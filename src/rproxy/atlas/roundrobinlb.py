from .baselb import BaseLoadBalancer
from .server import OriginServer

class RoundRobinLoadBalancer(BaseLoadBalancer):
    def __init__(self, servers: dict[str, OriginServer] = None):
        super().__init__(servers)
        self.current_index = 0
        
    async def get_next_server(self):
        host = self.hosts[self.current_index]
        async with self.lock:
            self.current_index = (self.current_index + 1) % len(self.hosts)
        return self.servers[host]