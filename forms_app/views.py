from django.shortcuts import render, HttpResponse
from .forms import FormContatto

# Create your views here.
def contatto(request):
    #se la richiesta è di tipo post, quindi il client fa la richiesta inviando dei dati.
    if request.method == "POST":
        form = FormContatto(request.POST) #creazione del form

        if form.is_valid(): #is_valid() controlla se il form è valido

            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)


            #ritorna una pagina con un testo h1
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")

    else: 
        form = FormContatto()

    context = {
        "form" : form
    }
    return render(request, "forms_app/contatto.html", context)

