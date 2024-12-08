from django.urls import path
from service import views

urlpatterns = [
    path("", views.load_balance, name="load_balance"),
]