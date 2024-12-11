from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
async def default(request, path):
    return HttpResponse(f"Success! /{path}")