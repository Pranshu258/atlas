import random
import aiohttp
import time
from django.http import HttpResponse
from ..common.baselb import BaseLoadBalancer
from ..common.originserver import OriginServer

class PrequalLoadBalancer(BaseLoadBalancer):
    """
    A load balancer that selects the origin server based on Google's Prequal algorithm.
    https://research.google/pubs/load-is-not-what-you-should-balance-introducing-prequal/
    """
    def __init__(self, servers: dict[str, OriginServer] = None):
        """
        Initialize the prequal load balancer with the given servers.
        
        Args:
            servers (dict[str, OriginServer]): A dictionary of servers with hostnames as keys and OriginServer instances as values.
        """
        super().__init__(servers)
        self.probes = []

    async def forward_request(self, request, path: str):
        """
        Forward the request to the appropriate origin server based on the load balancing algorithm.
        The algorithm is implemented in the derived classes. This method also maintains the requests-in-flight count and the exponential moving average of latency for each server.

        Args:
            request (HttpRequest): The incoming HTTP request.
            path (str): The path to forward the request to.

        Returns:
            HttpResponse: The response from the origin server.
        """
        if not self.servers or len(self.servers) == 0:
            return HttpResponse("Service unavailable, please try again after some time.", status=503)
        
        origin = await self.get_next_server()
        url = f"http://{origin.host}/{path}"

        async with origin.lock:
            origin.local_rif += 1
         
        request_start_time = time.time()
        async with aiohttp.ClientSession(trust_env=True) as session: 
            async with session.get(url) as response:
                response = await response.text()
        request_end_time = time.time()
        elapsed_time = request_end_time - request_start_time

        async with origin.lock:
            origin.local_rif -= 1
            origin.latency = (elapsed_time + origin.latency)/2

        self.update_probe_pool(origin )

        proxyResponse = HttpResponse(response)
        proxyResponse["X-Atlas-Origin-Server"] = origin.host
        return proxyResponse
        
    def update_probe_pool(self):
        """
        Update the probe pool with the latest latency and RIF values.
        """
        if len(self.probes) < 16:
            self.probes = list(self.servers.values())
            return
        return None

    async def get_next_server(self):
        """
        Get the next origin server based on Google's Prequal algorithm.
        
        Returns:
            OriginServer: The next server to handle the request.
        """
        return self.servers[random.choice(self.hosts)]