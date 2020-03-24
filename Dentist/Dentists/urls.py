from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='hi'),
    path('contact.html', views.contact, name='contact'),
]