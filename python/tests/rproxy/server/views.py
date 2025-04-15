import json
from django.http import HttpResponse
from .apps import ServerConfig
from django.views.decorators.http import require_http_methods
from atlaslb.common.originserver import OriginServer

@require_http_methods(["POST"])
async def register(request):
    data = json.loads(request.body)
    server = OriginServer(host=data.get('host'), weight=data.get('weight'))
    await ServerConfig.loadbalancer.add_server(server)
    return HttpResponse("Current State: " + str(ServerConfig.loadbalancer))

async def forward(request, path):
    return await ServerConfig.loadbalancer.forward_request(request, path)