from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime

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

def queryBase(request):
    #1. Tutti gli articoli scritti da giornalisti di un certo cognome:
    articoli_cognome = Articolo.objects.filter(giornalista__cognome='Rossi') #filter() ritorna una lista di oggetti, se non ci sono oggetti con cognome rossi, ritornerà una lista vuota
    
    #2. Totale
    numero_totale_articoli = Articolo.objects.count() #count() ritorna il numero di oggetti presenti nel db
    
    #3. Contare il numero di articoli scritti da un giornalista specifico:
    try:
        giornalista_1 = Giornalista.objects.get(id=2) # ritorna un oggetto con id=2, se non esiste va nel blocco except
        numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista=giornalista_1).count()#conta la lunghezza della lista ritornata da filter()
    except Giornalista.DoesNotExist: #eccezione che può lanciare il metodo .get()
        numero_articoli_giornalista_1 = 0

    #4. Ordinare gli articoli per numero di visualizzazione in modo decrescente:
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni') #order_by() ordina i risultati, in questo caso mettendo il - davanti alla condizione li ordina in modo descrescente

    #5. Tutti gli articoli che non hanno visualizzazioni:
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)

    #6. Articolo più visualizzato
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()# first() Restituisce il primo elemento dell'order_by(-visualizzazioni).

    #7. Tutti i giornalisti nati dopo una certa data:
    giornalisti_data = Giornalista.objects.filter(anno_nascita__gt=datetime.date(1990, 1, 1))

    #8. Tutti gli articoli pubblicati in una data specifica
    articoli_del_giorno = Articolo.objects.filter(data_articolo=datetime.date(2023, 1, 1))

    #9. Tutti gli articoli pubblicati in un intervallo di date
    articoli_periodo = Articolo.objects.filter(data_articolo__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))

    #10. Gli articoli scritti da giornalisi nati prima del 1980:
    giornalisti_nati = Giornalista.objects.filter(anno_nascita__lt=datetime.date(1980, 1, 1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)

    #11. Il giornalista più giovane:
    giornalista_giovane = Giornalista.objects.order_by('anno_nascita').first()

    #12. Il giornalista più anziano:
    giornalista_anziano = Giornalista.objects.order_by('-anno_nascita').first()

    #13. Gli ultimi 5 articoli pubblicati:
    ultimi = Articolo.objects.order_by('-data_articolo')[:5] #[:5] limita il risultato ai primi 5

    #14. Tutti gli articoli con un certo numero minimo di visualizzazioni:
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)

    #15. Tutti gli articoli che contengono una certa parola nel titolo:
    articoli_parola = Articolo.objects.filter(titolo__icontains='importante')

    #16. Articoli pubblicati in un certo mese di un anno specifico
    articoli_mese_anno = Articolo.objects.filter(data__month=1, data__year=2023) #restituisce una lista

    #17. Giornalisti con almeno un articolo con più di 100 visualizzazioni
    giornalisti_con_articoli_popolari = Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct
    
    data = datetime.date(1990,1,1)
    visualizzazioni = 50
    #18. scrivi quali articoli vengono selezionati
    articoli_con_and = Articolo.objects.filter(giornalista__anno_di_nascita__gt=data, visualizzazioni__gte=visualizzazioni)

    from django.db.models import Q
    #19. scrivi quali articoli vengono selezionati
    articoli_con_or = Articolo.objects.filter(giornalista__anno_di_nascita__gt=data) | Q(visualizzazioni__lte=visualizzazioni)
    
    #Dizionazio Contenxt
    context = {
        'articoli_cognome' : articoli_cognome,
        'numero_totale_articoli' : numero_totale_articoli,
        'numero_articoli_giornalista_1' : numero_articoli_giornalista_1,
        'articoli_ordinati' : articoli_ordinati,
        'articoli_senza_visualizzazioni' : articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato' : articolo_piu_visualizzato,
        'giornalisti_data' : giornalisti_data,
        'articoli_del_giorno' : articoli_del_giorno,
        'articoli_periodo' : articoli_periodo,
        'articoli_giornalisti' : articoli_giornalisti,
        'giornalista_giovane' : giornalista_giovane,
        'giornalista_anziano' : giornalista_anziano,
        'ultimi' : ultimi,
        'articoli_minime_visualizzazioni' : articoli_minime_visualizzazioni,
        'articoli_parola' : articoli_parola,
        'articoli_mese_anno' : articoli_mese_anno,
        'giornalisti_con_articoli_popolari' : giornalisti_con_articoli_popolari,
        'articoli_con_and' : articoli_con_and,
        'articoli_con_or' : articoli_con_or
    }
    return render(request, 'news/query_base.html', context)