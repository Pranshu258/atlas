import asyncio
from .originserver import OriginServer
from django.http import HttpResponse
import aiohttp
import time

class BaseLoadBalancer:
    def __init__(self, servers: dict[str, OriginServer] = None):
        self.servers = servers if servers is not None else {}
        self.hosts = list(self.servers.keys())
        self.lock = asyncio.Lock()

    async def add_server(self, server: OriginServer):
        async with self.lock:
            if server.host not in self.servers:
                self.hosts.append(server.host)
            self.servers[server.host] = server

    async def forward_request(self, request, path: str):
        if not self.servers or len(self.servers) == 0:
            return HttpResponse("Service unavailable, please try again after some time.", status=503)
        
        origin = await self.get_next_server()
        url = f"http://{origin.host}/{path}"

        async with origin.lock:
            origin.local_rif += 1
         
        request_start_time = time.time()
        async with aiohttp.ClientSession() as session: 
            async with session.get(url) as response:
                response = await response.text()
        request_end_time = time.time()
        elapsed_time = request_end_time - request_start_time

        async with origin.lock:
            origin.local_rif -= 1
            origin.latency = elapsed_time + origin.latency/2

        proxyResponse = HttpResponse(response)
        proxyResponse["X-Atlas-Origin-Server"] = origin.host
        return proxyResponse
        
    def __str__(self):
        return ", ".join([str(server) for server in self.servers.values()])