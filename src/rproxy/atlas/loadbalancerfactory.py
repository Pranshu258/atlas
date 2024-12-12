from .roundrobinlb import RoundRobinLoadBalancer
from .randomlb import RandomLoadBalancer
from .weightedroundrobinlb import WeightedRoundRobinLoadBalancer

class LoadBalancerFactory: 
    def CreateLoadBalancer(self, configuration):
        match configuration['lb_type']:
            case 'random':
                return RandomLoadBalancer(configuration['servers'])
            case 'roundrobin':
                return RoundRobinLoadBalancer(configuration['servers'])
            case 'weightedroundrobin':
                return WeightedRoundRobinLoadBalancer(configuration['servers'], weights=configuration['weights'])
            case _:
                raise ValueError(f"Unknown load balancer type: {configuration['lb_type']}")