from django.urls import path
from employees_app.employees.views import hr_department, production_department, accounting_department, \
    r_and_d_department, employees_by_department_id, employees_home_page

urlpatterns = [
    path('', employees_home_page, name='employees_index'),
    path('hr/<str:name>', hr_department, name='hr'),
    path('production/', production_department, name='production'),
    path('accounting/', accounting_department, name='accounting'),
    path('r&d/', r_and_d_department, name='r&d'),
    path('<int:department_number>/', employees_by_department_id, name='employees_by_id')
]