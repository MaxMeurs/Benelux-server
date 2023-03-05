from django.urls import path, include
from . import views
urlpatterns = [
    path('LOLhome', views.LeagueOfLegends, name='LOLhome'),
]