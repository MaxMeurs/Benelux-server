from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'BeneluxRL/home.html')


def over_ons(request):
    return render(request, 'BeneluxRL/over-ons.html')
