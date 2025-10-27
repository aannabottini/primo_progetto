from django.shortcuts import render

# Create your views here.

#funzione che verrà associata all'url della pagina homepage
def homepage(request): #request: un oggetto contenente le informazioni relative alla richiesta fatta dal client
    return render(request, "prima_app/homepage.html") #render: una funzione usata per inviare al client una pagina html.

#funzione che verrà associata alla pagina welcome
def welcome(request):
    return render(request, "prima_app/welcome.html") 

#funzione che verrà associata alla pagina lista
def lista(request):
    return render(request, "prima_app/lista.html") 

#funzione che verrà associata alla pagina chi_siamo
def chi_siamo(request):
    return render(request, "prima_app/chi_siamo.html")

#funzione che verrà associata alla pagina variabili
def variabili(request):
    context = {
        'var1' : 'Prima variabile',
        'var2' : 'Seconda variabile',
        'var3' : 'Terza variabile'
    }
    return render(request, "prima_app/variabili.html", context)

#funzione che verrà associata alla pagina index
def index(request):
    return render(request, "prima_app/index.html")