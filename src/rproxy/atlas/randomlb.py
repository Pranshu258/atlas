import random
from .baselb import BaseLoadBalancer

class RandomLoadBalancer(BaseLoadBalancer):
    def __init__(self, servers):
        super().__init__(servers)
        
    def get_next_server(self):
        return random.choice(self.servers)