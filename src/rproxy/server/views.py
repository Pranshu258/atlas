from django.http import HttpResponse
import atlas.apps as Atlas
from .apps import ServerConfig

def register(request):
    message = Atlas.AtlasConfig.name
    ServerConfig.loadbalancer.add_server("127.0.0.1:8003")
    return HttpResponse("Hello! " + message)
