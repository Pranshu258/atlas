from django.apps import AppConfig
import atlas.loadbalancerfactory as LoadBalancerFactory

class ServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server'
    loadbalancer = LoadBalancerFactory.LoadBalancerFactory().CreateLoadBalancer(
        {'lb_type': 'roundrobin', 'servers': ['127.0.0.1:8001', '127.0.0.1:8002']}
    )