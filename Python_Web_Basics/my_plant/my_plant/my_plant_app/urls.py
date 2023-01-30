from django.urls import path

from my_plant.my_plant_app.views import show_home, show_catalogue, create_profile, details_profile, edit_profile, \
    delete_profile, create_plant, details_plant, edit_plant, delete_plant

urlpatterns = (
    path('', show_home, name='index'),
    path('catalogue/', show_catalogue, name='show catalogue'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', details_profile, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>/', details_plant, name='plant details'),
    path('edit/<int:pk>/', edit_plant, name='edin plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
)