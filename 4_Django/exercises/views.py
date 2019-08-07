from exercises.models import Band
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from exercises.temperature_functions import oblicz_celc_to_fahr, oblicz_fahr_to_celc

def show_band(request, id):
    band = Band.objects.get(id=id)

    return render(request, 'show_band.html', {'band': band})


def tabliczka_mnozenia(request):
    height = int(request.GET['height'])
    width = int(request.GET['width'])
    ret_list = []
    for i in range(1,height+1):
        temp_list = []
        for j in range(1,width+1):
            temp_list.append(i*j)
        ret_list.append(temp_list)
    return render(request, 'tm.html', {'tm':ret_list})


@csrf_exempt
def imie(request):
    if request.method == 'GET':
        html = """
        <form method = 'post'>
        imie:<input type='text' name='name'>
        nazwisko:<input type='text' name='last_name'>
        <input type='submit' value='go go go reko gadgeta'>
        """
        return HttpResponse(html)
    else:
        name = request.POST['name']
        ln = request.POST["last_name"]
        return HttpResponse(f'witaj {name} {ln}!!! ')

@csrf_exempt
def temp(request):
    if request.method == 'POST':
        degrees = float(request.POST['degrees'])
        direction = request.POST['convertionType']
        if direction == 'celcToFahr':
            ret_val = f'celcjusz {degrees}  to Fahr {oblicz_celc_to_fahr(degrees)}'
        else:
            ret_val = f'fahr {degrees}  to celc {oblicz_fahr_to_celc(degrees)}'
        return HttpResponse(ret_val)
    else:
        return render(request, 'temp.html')


def show_session(request):
    if 'counter' in request.session:
        request.session['counter']+=1
        return HttpResponse (f"jupika jej zmienna counter = {request.session['counter']}")
    return HttpResponse("zmienna counter nie istneje")


def set_session(request):
    request.session['counter'] = 1
    request.session['sadfkldsajhf'] = 'dupa'
    return HttpResponse("udało sie ustawić sessje")

def del_session(request):
    del request.session['counter']
    return HttpResponse("udało sie skasować sessje")


def show_cookie(request):
    if 'counter' in request.cookie:
        request.session['counter']+=1
        return HttpResponse (f"jupika jej zmienna counter = {request.session['counter']}")
    return HttpResponse("zmienna counter nie istneje")


def set_session(request):
    request.session['counter'] = 1
    request.session['sadfkldsajhf'] = 'dupa'
    return HttpResponse("udało sie ustawić sessje")

def del_session(request):
    del request.session['counter']
    return HttpResponse("udało sie skasować sessje")
