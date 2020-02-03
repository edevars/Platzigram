# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utils
from datetime import datetime


def hello_world(request):
    return HttpResponse('Hello world')


def see_date_time(request):
    now = datetime.now().strftime('%dth %b, %Y - %H:%Mhrs')
    return HttpResponse(f'Oh! La fecha de hoy es {str(now)}')


def sort_numbers(request):
    numbers = request.GET['numbers']
    numbers_list = numbers.split(',')
    sorted_numbers = list(int(number) for number in numbers_list)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Intergers Sorted'
    }
    return JsonResponse(data)


def get_access_by_age(request, name, age):
    message = ''
    if age >= 18:
        message = f'Bienvenido de nuevo {name}!'
    else:
        message = f'Acceso no permitido a menores de 18, lo lamentamos {name}'

    return HttpResponse(message)
