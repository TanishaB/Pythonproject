from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name="hi"),
    path('hi.html', views.hi, name="hi"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),
    path('pricing.html', views.pricing, name="pricing"),
    
]
