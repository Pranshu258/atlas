import asyncio
import aiohttp
from django.http import HttpResponse
from .apps import ServerConfig
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
async def register(request):
    try:
        data = await request.json()
        server_name = data.get('origin_host')
        if not server_name:
            return HttpResponse("Invalid request - Origin host name not provided.", status=400)
    except Exception as e:
        return HttpResponse(f"Error reading request body: {str(e)}", status=400)
    
    await ServerConfig.loadbalancer.add_server(server_name)
    return HttpResponse("Current State: " + ServerConfig.loadbalancer.servers.__str__())

async def forward(request, path):
    origin = await ServerConfig.loadbalancer.get_next_server()
    url = f"http://{origin}/{path}" 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url) as response:
            originalResponse = await response.text()
            return HttpResponse(f"Response from {origin}: {originalResponse}")