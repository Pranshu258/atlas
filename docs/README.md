# Atlas
Atlas is a reverse proxy based load balancing framework implemented in Python. It exposes various load balancing algorithms to distribute incoming requests across multiple origin servers. The load balancer state is maintained in-memory at the reverse proxy server, with no (or minimal) set up needed on the origin server.

## Installation
Atlas can be installed from the Python Package Index using the following command: 
```
pip install atlaslb
```

## Supported Algorithms
1. [Random](./random.md)
2. [Round Robin](./roundrobin.md)
3. [Least Connection](./leastconnection.md)
4. [Least Latency](./leastlatency.md)

## OriginServer
The `OriginServer` class represents an origin server with various attributes such as host, weight, CPU usage, local requests in flight (local_rif), and latency.

#### Methods
- `__init__(self, host, weight=1, cpu=0, local_rif=0, latency=0)`: Initializes the origin server with the given attributes.
- `__str__(self)`: Returns a string representation of the origin server.

## LoadBalancerFactory
The `LoadBalancerFactory` class is a factory class to create different types of load balancers based on the given configuration.

#### Methods
- `CreateLoadBalancer(self, configuration)`: Creates a load balancer based on the provided configuration.