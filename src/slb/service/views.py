from django.http import HttpResponse

def load_balance(request):
    return HttpResponse("Hi, welcome to the frontdoor, slb service is up and running")