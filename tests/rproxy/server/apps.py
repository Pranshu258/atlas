from django.apps import AppConfig
from atlaslb.common.loadbalancerfactory import LoadBalancerFactory

class ServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server'
    loadbalancer = LoadBalancerFactory().CreateLoadBalancer(
        {'algorithm': 'roundrobin', 'servers': None}
    )