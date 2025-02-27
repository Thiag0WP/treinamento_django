from . import views
from django.urls import path

urlpatterns = [
    path('helloworld/', views.home, name='home'),
]