from .baselb import BaseLoadBalancer
from .originserver import OriginServer

class RoundRobinLoadBalancer(BaseLoadBalancer):
    """
    A load balancer that selects the origin server in a round-robin fashion.
    """
    def __init__(self, servers: dict[str, OriginServer] = None):
        super().__init__(servers)
        self.current_index = 0
        
    async def get_next_server(self):
        """
        Get the next origin server based on the round-robin selection algorithm.
        """
        host = self.hosts[self.current_index]
        async with self.lock:
            self.current_index = (self.current_index + 1) % len(self.hosts)
        return self.servers[host]