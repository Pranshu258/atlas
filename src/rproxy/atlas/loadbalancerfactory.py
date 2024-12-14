from .roundrobinlb import RoundRobinLoadBalancer
from .randomlb import RandomLoadBalancer
from .weightedroundrobinlb import WeightedRoundRobinLoadBalancer
from .leastconnectionlb import LeastConnectionLoadBalancer
from .leastconnectionpoweroftwolb import LeastConnectionPowerOfTwoLoadBalancer
from .leastlatencylb import LeastLatencyLoadBalancer
from .leastlatencypoweroftwolb import LeastLatencyPowerOfTwoLoadBalancer

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
            case 'leastlatency':
                return LeastLatencyLoadBalancer(configuration['servers'])
            case 'leastlatencypoweroftwo':
                return LeastLatencyPowerOfTwoLoadBalancer(configuration['servers'])
            case _:
                raise ValueError(f"Unknown load balancer algorithm: {configuration['algorithm']}")