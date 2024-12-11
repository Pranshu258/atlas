from .baselb import BaseLoadBalancer

class RoundRobinLoadBalancer(BaseLoadBalancer):
    def __init__(self, servers):
        super().__init__(servers)
        self.current_index = 0
        
    def get_next_server(self):
        with self.lock:
            server = self.servers[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.servers)
        return server