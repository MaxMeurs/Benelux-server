from django.urls import path, include
from . import views

urlpatterns = [
    path('RLhome', views.rocketleagehome, name='RLhome'),

]
