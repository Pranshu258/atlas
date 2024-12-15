# Atlas

## Introduction
Atlas is a load balancing framework that provides various load balancing algorithms to distribute incoming requests across multiple origin servers. The framework includes several load balancers such as Round Robin, Random, Least Connection, Least Latency, and their variations using the power of two choices algorithm.

## Load Balancers

### BaseLoadBalancer
The `BaseLoadBalancer` class is the base class for all load balancers. It maintains a list of origin servers and a mapping of hostnames to server objects.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the load balancer with the given servers.
- `add_server(self, server: OriginServer)`: Adds a server to the load balancer.
- `forward_request(self, request, path: str)`: Forwards the request to the appropriate origin server based on the load balancing algorithm.
- `__str__(self)`: Returns a string representation of the load balancer.

### RoundRobinLoadBalancer
The `RoundRobinLoadBalancer` class selects the origin server in a round-robin fashion.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the round-robin load balancer with the given servers.
- `get_next_server(self)`: Gets the next origin server based on the round-robin selection algorithm.

### RandomLoadBalancer
The `RandomLoadBalancer` class selects the origin server randomly.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the random load balancer with the given servers.
- `get_next_server(self)`: Gets the next origin server based on the random selection algorithm.

### LeastConnectionLoadBalancer
The `LeastConnectionLoadBalancer` class selects the origin server with the least number of active connections.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the least connection load balancer with the given servers.
- `get_next_server(self)`: Gets the next server with the least number of active connections.

### LeastLatencyLoadBalancer
The `LeastLatencyLoadBalancer` class selects the origin server with the least latency.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the least latency load balancer with the given servers.
- `get_next_server(self)`: Gets the next server with the least latency.

### LeastConnectionPowerOfTwoLoadBalancer
The `LeastConnectionPowerOfTwoLoadBalancer` class selects the origin server with the least number of active connections using the power of two choices algorithm.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the least connection power of two load balancer with the given servers.
- `get_next_server(self)`: Gets the next server with the least number of active connections using the power of two choices algorithm.

### LeastLatencyPowerOfTwoLoadBalancer
The `LeastLatencyPowerOfTwoLoadBalancer` class selects the origin server with the least latency using the power of two choices algorithm.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the least latency power of two load balancer with the given servers.
- `get_next_server(self)`: Gets the next server with the least latency using the power of two choices algorithm.

### WeightedRoundRobinLoadBalancer
The `WeightedRoundRobinLoadBalancer` class selects the origin server in a weighted round-robin fashion. Servers with higher weights will be selected more frequently.

#### Methods
- `__init__(self, servers: dict[str, OriginServer] = None)`: Initializes the weighted round-robin load balancer with the given servers.
- `get_next_server(self)`: Gets the next server in a weighted round-robin fashion.

## OriginServer
The `OriginServer` class represents an origin server with various attributes such as host, weight, CPU usage, local requests in flight (local_rif), and latency.

#### Methods
- `__init__(self, host, weight=1, cpu=0, local_rif=0, latency=0)`: Initializes the origin server with the given attributes.
- `__str__(self)`: Returns a string representation of the origin server.

## LoadBalancerFactory
The `LoadBalancerFactory` class is a factory class to create different types of load balancers based on the given configuration.

#### Methods
- `CreateLoadBalancer(self, configuration)`: Creates a load balancer based on the provided configuration.