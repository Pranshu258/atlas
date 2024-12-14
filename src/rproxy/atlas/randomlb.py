import random
from .baselb import BaseLoadBalancer
from .originserver import OriginServer

class RandomLoadBalancer(BaseLoadBalancer):
    """
    A load balancer that selects the origin server randomly.
    """
    def __init__(self, servers: dict[str, OriginServer] = None):
        super().__init__(servers)
        
    async def get_next_server(self):
        """
        Get the next origin server based on the random selection algorithm.
        """
        return self.servers[random.choice(self.hosts)]