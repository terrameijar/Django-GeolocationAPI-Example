from django.shortcuts import render # This is used to render the template
import requests # We'll use this to connect to the IP-API
from django.conf import settings


def home(request):
    is_cached = ('geodata' in request.session)

    if not is_cached:
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
        response = requests.get(f'http://ip-api.com/json/{user_ip}')
        request.session['geodata'] = response.json()


    geodata = request.session['geodata']

    context = {
        'ip': geodata['query'],
        'country': geodata['country'],
        'latitude': geodata['lat'],
        'longitude': geodata['lon'],
        'api_key': settings.API_KEY,
        'is_cached': is_cached,
    }

    return render(request, 'home.html', context)


def search_ip(request):

    if request.method == 'GET' and 'ip' in request.GET:
        ip_address = request.GET['ip']
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        geodata = response.json()

        context = {
            'ip': geodata['query'],
            'country': geodata['country']
        }

        return render(request, 'search.html', context)

    return render(request, 'search.html')

