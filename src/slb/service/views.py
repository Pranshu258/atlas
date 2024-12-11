from django.http import HttpResponse
from apps import loadbalancer

def register(request):
    message = loadbalancer.add_server("randomhostname")
    return HttpResponse(message)

def forward(request, path):
    return HttpResponse("Hi, welcome to the frontdoor, slb service is up and running")