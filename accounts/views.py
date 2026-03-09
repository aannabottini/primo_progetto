from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login

# Create your views here.
def signup(request): 
    if request.method == 'POST': #controlla se il form è stato inviato
        form = SignUpForm(request.POST) 

        if form.is_valid(): #controlla che i dati siano validi
            user = form.save() # form.save() salva l'utente nel db e ritorna un oggetto salvato nella variabile user
            login(request, user) # effettua il login automatico
            return redirect('/') # reindirizza alla home
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form' : form})


'''
---PRIMA VERSIONE---

def signup(request):  
    if request.method == 'POST': #controlla se il form è stato inviato
            form = SignUpForm(request.POST) 

            if form.is_valid(): #controlla che i dati siano validi
                form.save() #salva il nuovo utente nel database
                return redirect('login') #dopo aver salvato l'utente reinderizza l'utente alla pagina login
        else: #richiesta di tipo get
            form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

'''
    