from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.index, name='index'),
    # path('', views.home, name='home'),
]


