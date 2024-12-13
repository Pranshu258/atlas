import random
from .baselb import BaseLoadBalancer
from .server import OriginServer

class RandomLoadBalancer(BaseLoadBalancer):
    def __init__(self, servers: dict[str, OriginServer] = None):
        super().__init__(servers)
        
    async def get_next_server(self):
        return self.servers[random.choice(self.hosts)]