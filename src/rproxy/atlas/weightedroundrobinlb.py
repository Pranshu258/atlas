import numpy as np
from math import gcd
from functools import reduce
from .baselb import RoundRobinLoadBalancer

class WeightedRoundRobinLoadBalancer(RoundRobinLoadBalancer):
    def __init__(self, servers, weights):
        super().__init__(servers)
        self.weights = np.divide(weights, reduce(gcd, weights))
        self.current_repeat_count = 0
        
    async def get_next_server(self):
        async with self.lock:
            server = self.servers[self.current_index]
            self.current_repeat_count += 1
            if self.current_repeat_count >= self.weights[self.current_index]:
                self.current_index = (self.current_index + 1) % len(self.servers)
                self.current_repeat_count = 0
        return server