from django.apps import AppConfig

class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service'
    configuration = {
        'lb_type': 'roundrobin',
        'servers': ['localhost:8000', 'localhost:8001', 'localhost:8002']
    }

    def ready(self):
        from slb.atlaslb.loadbalancerfactory import LoadBalancerFactory
        loadbalancer = LoadBalancerFactory.CreateLoadBalancer(self, self.configuration)