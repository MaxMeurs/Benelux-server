from django.shortcuts import render, redirect


# Create your views here.

def LeagueOfLegends(request):
    return render(request, "LOL/home.html")
