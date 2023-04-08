from django.urls import path
from . import views

urlpatterns = [
    path('hello_app2', views.hello_world_app2),
]