from django.shortcuts import render, redirect


# Create your views here.
def rocketleagehome(request):
    return render(request, 'RL/home.html')
