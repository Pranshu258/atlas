import asyncio
from django.http import HttpResponse
from .apps import ServerConfig

async def register(request):
    await ServerConfig.loadbalancer.add_server("127.0.0.1:8003")
    return HttpResponse("Current State: " + ServerConfig.loadbalancer.servers.__str__())

async def forward(request, path):
    origin = await ServerConfig.loadbalancer.get_next_server()
    return HttpResponse("Forwarding request to server " + origin + " for path " + path)