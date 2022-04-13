from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect


def home(request):
    return HttpResponse('This is Home!')


def marketing_department(request):

    return HttpResponse('This is Marketing!')


def hr_department(request, hr_id):
    if hr_id < 10:
        return HttpResponse('This is HR!')
    else:
        return HttpResponseNotFound('Out of range')


def production_department(request, pk):
    if pk < 10:
        return HttpResponse('This is Production!')
    else:
        return redirect(to='home')


def accounting_department(request):
    return HttpResponse('This is accounting!')


def main_employees(request):
    return HttpResponse('This is Main!')
