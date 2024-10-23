from django.urls import path
# from newapp.apps import NewappConfig
from . import views
from myproject.catalog.views import home, contacts
# app_name = NewappConfig.name
app_name = 'catalog'

urlspatterns = [
    path('',),
    path('', home, name='home'),
    path('', contacts, name='contacts'),
    # path('home/', views.home, name='home'),
    # path('about/', views.about, name='about'),
]
