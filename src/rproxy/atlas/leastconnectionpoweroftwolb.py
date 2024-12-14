from .originserver import OriginServer
from .baselb import BaseLoadBalancer
import random

class LeastConnectionPowerOfTwoLoadBalancer(BaseLoadBalancer):
    def __init__(self, servers: dict[str, OriginServer] = None):
        super().__init__(servers)
        
    async def get_next_server(self):
        if len(self.hosts) == 1:
            return self.servers[self.hosts[0]]
        else:
            candidates = random.sample(self.hosts, 2)
            if self.servers[candidates[0]].local_rif < self.servers[candidates[1]].local_rif:
                return self.servers[candidates[0]]
            else:
                return self.servers[candidates[1]]