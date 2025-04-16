namespace Atlas.LoadBalancer.Algorithms;

public interface ILoadBalancingStrategy
{
    string SelectServer(List<string> servers);
}