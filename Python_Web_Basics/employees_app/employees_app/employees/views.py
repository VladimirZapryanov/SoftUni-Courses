<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def home(request):
    return HttpResponse('This is HOME!!!')


def employees_home_page(request):
    context = {'employees': {'Vladimir Zapryanov': '1',
                             'Martin Ivanov': '2',
                             },
               'department': 'Marketing',
               }

    return render(request, 'employees_index.html', context)


def hr_department(request, name):

    if len(name) > 10:
        raise Exception('Not correct name!!!')
    else:
        return HttpResponse(f'This is HR {name.upper()}')


def production_department(request):
    return HttpResponse('This is PRODUCTION_DEPARTMENT!')


def accounting_department(request):
    return HttpResponse('This is ACCOUNTING_DEPARTMENT!')


def r_and_d_department(request):
    return HttpResponse('This is R&D_DEPARTMENT!')


def employees_by_department_id(request, department_number):
    employee = ''
    if department_number == 1:
        employee = 'Vladimir Zapryanov'
    elif department_number == 2:
        employee = 'Martin Ivanov'
    else:
        employee = 'Unknown employee'

    html = '<html><body><h1>Employees: %s, ' \
           'Department: %s</h1></body></html>' \
           % (employee, department_number)

    if not employee == 'Unknown employee':
        return HttpResponse(html)
    else:
        return redirect(to='employees_index')

=======
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def home(request):
    return HttpResponse('This is HOME!!!')


def employees_home_page(request):
    context = {'employees': {'Vladimir Zapryanov': '1',
                             'Martin Ivanov': '2',
                             },
               'department': 'Marketing',
               }

    return render(request, 'employees_index.html', context)


def hr_department(request, name):

    if len(name) > 10:
        raise Exception('Not correct name!!!')
    else:
        return HttpResponse(f'This is HR {name.upper()}')


def production_department(request):
    return HttpResponse('This is PRODUCTION_DEPARTMENT!')


def accounting_department(request):
    return HttpResponse('This is ACCOUNTING_DEPARTMENT!')


def r_and_d_department(request):
    return HttpResponse('This is R&D_DEPARTMENT!')


def employees_by_department_id(request, department_number):
    employee = ''
    if department_number == 1:
        employee = 'Vladimir Zapryanov'
    elif department_number == 2:
        employee = 'Martin Ivanov'
    else:
        employee = 'Unknown employee'

    html = '<html><body><h1>Employees: %s, ' \
           'Department: %s</h1></body></html>' \
           % (employee, department_number)

    if not employee == 'Unknown employee':
        return HttpResponse(html)
    else:
        return redirect(to='employees_index')

>>>>>>> 66de25c979112b7620fc63e8c310f7bad8311db5
