from django.urls import path
from .views import home, about, service, contact

urlpatterns = [
    path("", home, name='home'),
    path("about/", about, name='about'),
    path("service/", service, name='service'),
    path("contact/", contact, name='contact'),
]