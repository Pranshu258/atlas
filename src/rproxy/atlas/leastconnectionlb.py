from .baselb import BaseLoadBalancer
from .originserver import OriginServer

class LeastConnectionLoadBalancer(BaseLoadBalancer):
    def __init__(self, servers: dict[str, OriginServer] = None):
        super().__init__(servers)
        
    async def get_next_server(self):
        return self.servers[min(self.hosts, key=lambda x: self.servers[x].local_rif)]