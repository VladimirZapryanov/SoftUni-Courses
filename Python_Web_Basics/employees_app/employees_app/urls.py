<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from employees_app.employees.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('employees/', include('employees_app.employees.urls'))
]
=======
from django.contrib import admin
from django.urls import path, include
from employees_app.employees.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('employees/', include('employees_app.employees.urls'))
]
>>>>>>> 66de25c979112b7620fc63e8c310f7bad8311db5
