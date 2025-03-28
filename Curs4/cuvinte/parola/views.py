from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random
import string

import pandas as pd


CIFRE = [str(i) for i in range(10)]
LITERE_MARI = [chr(i) for i in range(ord('A'), ord('Z')+1)]
LITERE_MICI = [chr(i) for i in range(ord('a'), ord('a')+1)]



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

    OPTIONS = string.ascii_lowercase 
    if request.GET.get('withupper'):
        OPTIONS += string.ascii_uppercase
    if request.GET.get('withdigits'):
        OPTIONS += string.digits
    if request.GET.get('withspecial'):
        OPTIONS += string.punctuation


#+ string.ascii_uppercase + string.digits + string.punctuation
    print(lungime)
    try:
        lungime=int(lungime)
        parola = ""
        for i in range(lungime):
            parola += random.choice(OPTIONS)

        context['parola'] = parola

        df = pd.read_csv('parole.csv', index_col=0)
        df.loc[len(df)] = parola
        df.to_csv("parole.csv")
        print("df=", df)
    except:
        pass

    return render(request, "alege.html", context)