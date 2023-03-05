from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('over_ons', views.over_ons, name='over_ons'),
    path('contact', views.contact, name='contact'),

]