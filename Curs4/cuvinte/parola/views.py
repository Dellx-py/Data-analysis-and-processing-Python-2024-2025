from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random
import string


CIFRE = [str(i) for i in range(10)]
LITERE_MARI = [chr(i) for i in range(ord('A'), ord('Z')+1)]
LITERE_MICI = [chr(i) for i in range(ord('a'), ord('a')+1)]

OPTIONS = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

def random_view(request):
    OPTIUNI = CIFRE + LITERE_MICI + LITERE_MARI
    parola = ""
    for i in range(100):
        parola += random.choice(OPTIUNI)
    return HttpResponse(parola)

def alege_view(request):
    print(request.GET)

   
    context = {

    }
    lungime = request.GET.get('lungime')
    if lungime:
        parola = ""
        for i in range(100):
            parola += random.choice(OPTIONS)

        context['parola'] = '1234'

    return render(request, "alege.html", context)