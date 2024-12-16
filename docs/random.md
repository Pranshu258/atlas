# Random
The `RandomLoadBalancer` class selects the origin server randomly.

## Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the random load balancer with the given servers.
- `get_next_server(self)`: Gets the next origin server based on the random selection algorithm.