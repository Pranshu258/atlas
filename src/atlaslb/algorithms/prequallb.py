import random
from ..common.baselb import BaseLoadBalancer
from ..common.originserver import OriginServer

class PrequalLoadBalancer(BaseLoadBalancer):
    """
    A load balancer that selects the origin server based on Google's Prequal algorithm.
    """
    def __init__(self, servers: dict[str, OriginServer] = None):
        """
        Initialize the prequal load balancer with the given servers.
        
        Args:
            servers (dict[str, OriginServer]): A dictionary of servers with hostnames as keys and OriginServer instances as values.
        """
        super().__init__(servers)
        
    async def get_next_server(self):
        """
        Get the next origin server based on google's prequal algorithm.
        
        Returns:
            OriginServer: The next server to handle the request.
        """
        return self.servers[random.choice(self.hosts)]