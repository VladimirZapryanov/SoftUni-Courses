from django.shortcuts import render, redirect

from petstragram.main_app.models import Profile, PetPhoto, Pet


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pet_photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile).distinct()

    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)


def show_profile(request):
    profile = get_profile()
    pets = list(Pet.objects.filter(user_profile=profile))
    pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()

    pet_photos_count = len(pet_photos)
    total_likes = sum(pp.likes for pp in pet_photos)

    context = {
        'profile': profile,
        'pet_photos_count': pet_photos_count,
        'pet_photos_likes': total_likes,
    }
    return render(request, 'profile_details.html', context)


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('pet photo details', pk)


def create_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass


def create_pet(request):
    pass


def edit_pet(request):
    pass


def delete_pet(request):
    pass


def create_pet_photo(request):
    pass


def edit_pet_photo(request):
    pass


