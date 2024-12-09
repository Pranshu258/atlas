from django.http import HttpResponse
from atlaslb import registration

def register(request):
    message = registration.register("randomhostname")
    return HttpResponse(message)

def forward(request, path):
    return HttpResponse("Hi, welcome to the frontdoor, slb service is up and running")