from django.http import HttpResponse

def forward(request):
    return HttpResponse("Hi, welcome to the frontdoor, slb service is up and running")