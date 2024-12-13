from .roundrobinlb import RoundRobinLoadBalancer
from .server import OriginServer

class WeightedRoundRobinLoadBalancer(RoundRobinLoadBalancer):
    def __init__(self, servers: dict[str, OriginServer] = None):
        super().__init__(servers)
        self.current_repeat_count = 0
        
    async def get_next_server(self):
        host = self.hosts[self.current_index]
        async with self.lock:
            self.current_repeat_count += 1
            if self.current_repeat_count >= self.servers[host].weight:
                self.current_index = (self.current_index + 1) % len(self.hosts)
                self.current_repeat_count = 0
        return self.servers[host]