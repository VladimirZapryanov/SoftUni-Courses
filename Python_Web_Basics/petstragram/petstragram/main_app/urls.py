from django.urls import path

from petstragram.main_app.views import home, dashboard, profile_details, photo_details

urlpatterns = [
    path('', home, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile_details, name='profile details'),
    path('photo/details/<int:pk>', photo_details, name='photo details')
]

