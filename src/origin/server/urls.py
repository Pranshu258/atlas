from django.urls import path, re_path
from server import views

urlpatterns = [
    # catch-all pattern for request forwarding (must be last in the list)
    re_path(r'^(?P<path>.*)$', views.default, name="default")
]