# Round Robin
Round robin load balancing algorithm selects the origin server in a round robin fashion. Each new request goes to the next server in the list and then circles back to the first. A variation of the algorithm is when the servers have weights associated with them, which allows repeated selection of a server, before the algorithm moves on to the next. 

## Implementations
### Basic
The `RoundRobinLoadBalancer` class selects the origin server in a round-robin fashion. Each server is chosen exactly once before the next one is selected.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the round-robin load balancer with the given servers.
- `get_next_server(self)`: Gets the next origin server based on the round-robin selection algorithm.

### Weighted Round Robin
The `WeightedRoundRobinLoadBalancer` class selects the origin server in a weighted round-robin fashion. Servers with higher weights will be selected more frequently.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the weighted round-robin load balancer with the given servers.
- `get_next_server(self)`: Gets the next server in a weighted round-robin fashion.