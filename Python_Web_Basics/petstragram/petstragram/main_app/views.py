from django.shortcuts import render


def home(request):
    return render(request, 'home_page.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def profile_details(request):
    return render(request, 'profile_details.html')


def photo_details(request):
    return render(request, 'photo_details.html')

