from django.urls import path
from . import views

urlpatterns = [
    path('', views.members),
    path('position', views.positions),
]
