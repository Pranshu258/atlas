from django.urls import path, re_path
from service import views

urlpatterns = [
    path("register/", views.register, name="register"),
    # catch-all pattern for request forwarding (must be last in the list)
    re_path(r'^(?P<path>.*)$', views.forward, name="forward")
]