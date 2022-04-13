from django.urls import path

from employees_app.employees import views

urlpatterns = (
    path('marketing/', views.marketing_department, name='marketing_department'),
    path('hr/<int:hr_id>/', views.hr_department),
    path('production/<int:pk>/', views.production_department),
    path('accounting/', views.accounting_department),
    path('', views.main_employees, name='main')
)
