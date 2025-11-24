from django.shortcuts import render
import random

# Create your views here.
def indexProva(request):
      return render(request, "indexProva.html")

def maxmin(request):
      var1 = int(random.random()*10+1)
      var2 = int(random.random()*10+1)
      somma = var1+var2
      context = {
       'var1' : var1,
       'var2': var2, 
       'somma' : somma
    }
      return render(request, "maxmin.html", context)

def media(request):
      lista = []
      i = 0
      media = 0
      conta = 0
      for i in range(30):
         n = int(random.random()*10+1)
         media+=n
         lista.append(n)
         conta += 1 
      media = media/conta
      context = {
       'lista' : lista,
       'media' : media
    }
      return render(request, "media.html", context)