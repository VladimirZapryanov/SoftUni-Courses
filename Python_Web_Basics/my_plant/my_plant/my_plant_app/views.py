from django.shortcuts import render, redirect

from my_plant.my_plant_app.forms import CreateProfileForm, CreatePlantForm, EditProfileForm
from my_plant.my_plant_app.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profiles = get_profile()
    context = {
        'profile': profiles,
    }
    return render(request, 'home-page.html', context)


def show_catalogue(request):
    profiles = get_profile()
    context = {
        'profile': profiles,
    }
    return render(request, 'catalogue.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'create-profile.html', context)


def details_profile(request):
    profiles = get_profile()
    context = {
        'profile': profiles,
    }
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    return render(request, 'delete-profile.html')


def create_plant(request):
    profiles = get_profile()
    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')
    else:
        form = CreatePlantForm()

    context = {
        'form': form,
        'profile': profiles,
    }

    return render(request, 'create-plant.html', context)


def details_plant(request, pk):
    return render(request, 'plant-details.html')


def edit_plant(request, pk):
    return render(request, 'edit-plant.html')


def delete_plant(request, pk):
    return render(request, 'delete-plant.html')
