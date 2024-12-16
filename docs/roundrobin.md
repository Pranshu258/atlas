# Round Robin
The `RoundRobinLoadBalancer` class selects the origin server in a round-robin fashion.

## Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the round-robin load balancer with the given servers.
- `get_next_server(self)`: Gets the next origin server based on the round-robin selection algorithm.

# Weighted Round Robin
The `WeightedRoundRobinLoadBalancer` class selects the origin server in a weighted round-robin fashion. Servers with higher weights will be selected more frequently.

## Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the weighted round-robin load balancer with the given servers.
- `get_next_server(self)`: Gets the next server in a weighted round-robin fashion.