import asyncio

class BaseLoadBalancer: 
    def __init__(self, servers):
        self.servers = servers
        self.lock = asyncio.Lock()

    async def add_server(self, server):
        async with self.lock:
            if server not in self.servers:
                self.servers.append(server)