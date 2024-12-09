from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.index, name='index'),
    path('details', views.details, name='details'),
    path('contacts', views.contacts, name='contacts'),
    # path('', views.home, name='home'),
    # path('services', views.services, name='services'),
    # path('aboutus', views.index, name='aboutus'),
    # path('news', views.news, name='news'),
    # path('news_details', views.news_details, name='news_details'),
    # path('contact', views.contact, name='contact'),
    # path('form_contact', views.form_contact, name='form_contact'),
    # path('form_search', views.form_search, name='form_search'),
    # # path('search_result', views.search_result, name='search_result'),
    # path('form_newsletter', views.form_newsletter, name='form_newsletter'),
    # path('under_construction', views.under_construction, name='under_construction'),
    # path('set_custom_color', views.set_custom_color, name='set_custom_color'),
]


