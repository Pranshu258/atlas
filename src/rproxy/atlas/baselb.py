import asyncio
from .server import OriginServer

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

    def __str__(self):
        return ", ".join([str(server) for server in self.servers.values()])