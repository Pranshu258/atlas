### BaseLoadBalancer
The `BaseLoadBalancer` class is the base class for all load balancers. It maintains a list of origin servers and a mapping of hostnames to server objects.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the load balancer with the given servers.
- `add_server(self, server: OriginServer)`: Adds a server to the load balancer.
- `forward_request(self, request, path: str)`: Forwards the request to the appropriate origin server based on the load balancing algorithm.
- `__str__(self)`: Returns a string representation of the load balancer.

### RandomLoadBalancer
The `RandomLoadBalancer` class selects the origin server randomly.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the random load balancer with the given servers.
- `get_next_server(self)`: Gets the next origin server based on the random selection algorithm.