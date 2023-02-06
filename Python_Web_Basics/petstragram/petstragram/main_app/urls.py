<<<<<<< HEAD
from django.urls import path

from petstragram.main_app.views import show_home, show_dashboard, show_profile, show_pet_photo_details, like_pet_photo

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile, name='profile'),
    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
)

=======
from django.urls import path

from petstragram.main_app.views import show_home, show_dashboard, show_profile, show_pet_photo_details, like_pet_photo

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile, name='profile'),
    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
)

>>>>>>> c4cb2de84e4d95aeb5b1129c1cbc97122a654357
