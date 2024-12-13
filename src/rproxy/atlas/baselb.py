import asyncio
from .server import OriginServer
from django.http import HttpResponse
import aiohttp

class BaseLoadBalancer:
    def __init__(self, servers: dict[str, OriginServer] = None):
        self.servers = servers if servers is not None else {}
        self.hosts = list(self.servers.keys())
        self.lock = asyncio.Lock()

    async def add_server(self, server: OriginServer):
        async with self.lock:
            if server.host not in self.servers:
                self.servers[server.host] = server
                self.hosts.append(server.host)

    async def forward_request(self, request, path):
        if not self.servers:
            return HttpResponse("Service unavailable, please try again after some time.", status=503)
        
        origin = await self.get_next_server()
        url = f"http://{origin.host}/{path}"

        async with origin.lock:
            origin.local_rif += 1
         
        async with aiohttp.ClientSession() as session: 
            async with session.get(url) as response:
                originalResponse = await response.text()
                response = f"Response from {origin.host}: {originalResponse}"

        async with origin.lock:
            origin.local_rif -= 1

        return HttpResponse(response)
        
    def __str__(self):
        return ", ".join([str(server) for server in self.servers.values()])