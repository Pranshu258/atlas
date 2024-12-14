from .roundrobinlb import RoundRobinLoadBalancer
from .randomlb import RandomLoadBalancer
from .weightedroundrobinlb import WeightedRoundRobinLoadBalancer
from .leastconnectionlb import LeastConnectionLoadBalancer
from .leastconnectionpoweroftwolb import LeastConnectionPowerOfTwoLoadBalancer

class LoadBalancerFactory: 
    def CreateLoadBalancer(self, configuration):
        match configuration['algorithm']:
            case 'random':
                return RandomLoadBalancer(configuration['servers'])
            case 'roundrobin':
                return RoundRobinLoadBalancer(configuration['servers'])
            case 'weightedroundrobin':
                return WeightedRoundRobinLoadBalancer(configuration['servers'])
            case 'leastconnection':
                return LeastConnectionLoadBalancer(configuration['servers'])
            case 'leastconnectionpoweroftwo':
                return LeastConnectionPowerOfTwoLoadBalancer(configuration['servers'])
            case _:
                raise ValueError(f"Unknown load balancer algorithm: {configuration['algorithm']}")