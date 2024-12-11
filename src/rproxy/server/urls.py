from django.urls import path
from server import views

urlpatterns = [
    path("register/", views.register, name="register"),
]