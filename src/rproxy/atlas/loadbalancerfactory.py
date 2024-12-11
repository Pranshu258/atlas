from .roundrobinlb import RoundRobinLoadBalancer
from .randomlb import RandomLoadBalancer

class LoadBalancerFactory: 
    def CreateLoadBalancer(self, configuration):
        if configuration['lb_type'] == 'roundrobin':
            return RoundRobinLoadBalancer(configuration['servers'])
        else:
            return RandomLoadBalancer(configuration['servers'])