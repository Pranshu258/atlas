### LeastLatencyLoadBalancer
The `LeastLatencyLoadBalancer` class selects the origin server with the least latency.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the least latency load balancer with the given servers.
- `get_next_server(self)`: Gets the next server with the least latency.

### LeastLatencyPowerOfTwoLoadBalancer
The `LeastLatencyPowerOfTwoLoadBalancer` class selects the origin server with the least latency using the power of two choices algorithm.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the least latency power of two load balancer with the given servers.
- `get_next_server(self)`: Gets the next server with the least latency using the power of two choices algorithm.