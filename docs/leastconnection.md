# Least Connection
The `LeastConnectionLoadBalancer` class selects the origin server with the least number of active connections.

## Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the least connection load balancer with the given servers.
- `get_next_server(self)`: Gets the next server with the least number of active connections.

# Least Connection Power Of Two 
The `LeastConnectionPowerOfTwoLoadBalancer` class selects the origin server with the least number of active connections using the power of two choices algorithm.

## Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the least connection power of two load balancer with the given servers.
- `get_next_server(self)`: Gets the next server with the least number of active connections using the power of two choices algorithm.