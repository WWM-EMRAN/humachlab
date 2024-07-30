from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.index, name='index'),
    # path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('aboutus', views.index, name='aboutus'),
    path('news', views.news, name='news'),
    path('news_details', views.news_details, name='news_details'),
    path('contact', views.contact, name='contact'),
    path('newsletter', views.newsletter, name='newsletter'),
]


