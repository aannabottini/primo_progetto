from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Articolo, Giornalista
 
# Create your views here.

#Versione 1: ritorna una pagina html con contenuto "HomePage news!"
'''
def home(request):
    return HttpResponse("<h1>HomePage news!</h1>")
'''

#Versione 2: legge dal database e li mette in stringhe di codice html 
'''
def home(request):
    a=""
    g=""
    for art in Articolo.objects.all(): #Articolo.objects.all() è una funzione che ritorna una lista di oggetti Articolo del database
        a+=(art.titolo + "<br>")
    
    for gio in Giornalista.objects.all(): #stessa cosa di Articolo.objects.all() 
        g+=(gio.nome + "<br>")
    response = "Articoli:<br>" + a + "<br>Giornalisti:<br>"+g
    print(response)
    return HttpResponse("<h1>"+ response + "</h1>")
'''

#Versione3: legge dal database e li mette in liste di stringhe
'''
def home(request):
    a = []
    g = []
    for art in Articolo.objects.all(): #Articolo.objects.all() è una funzione che ritorna una lista di oggetti Articolo del database
        a.append(art.titolo)

    for gio in Giornalista.objects.all(): #stessa cosa di Articolo.objects.all() 
        g.append(gio.nome)

    response = str(a) + "<br>" + str(g)

    return HttpResponse("<h1>"+ response + "</h1>")
'''

#Versione4: 
def home(request):
    articoli = Articolo.objects.all() #articoli è la lista di articoli letti dal database
    giornalisti = Giornalista.objects.all() #uguale a articoli

    #definisco un dizionario perchè la funzione render del return richiede per forza un dizionario
    context = {"articoli": articoli,
               "giornalisti": giornalisti}
    return render(request, "news/homepage.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "news/articolo_detail.html", context)


def lista_articoli(request, pk=None):
    if(pk==None):
        intestazione="Tutti gli Articoli"
        articoli = Articolo.objects.all()
    else:
        intestazione="Articoli di un Giornalista"
        articoli = Articolo.objects.filter(giornalista_id=pk)
    context = {
        'intestazione': intestazione,
        'articoli': articoli,
    }
    return render(request, "news/lista_articoli.html", context)

'''
 quando non viene passato il parametro pk (primary key) del giornalista il suo valore sarà None
e quindi se pk==None utilizzerai  il metodo objects.all() altrimenti  il metodo objects.filter()
'''

