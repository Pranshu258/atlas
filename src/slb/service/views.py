from django.http import HttpResponse

def register(request):
    return HttpResponse("Register service")

def forward(request, path):
    return HttpResponse("Hi, welcome to the frontdoor, slb service is up and running")