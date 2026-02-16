from django.shortcuts import render

# Create your views here.
def index_voti(request):
    return render(request, 'voti/index_voti.html')

def lista_materie(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context = {
        'materie' : materie
    }
    return render(request, 'voti/lista_materie.html', context)

def lista_voti(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    context = { 
        'voti' : voti
    }
    return render(request, 'voti/lista_voti.html', context)

def media_voti(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

    media_voti = {}
    for studente, materie in voti.items():
        media = 0
        for materia,voto,assenze in materie:
            media+=voto
        media/=len(materie)
        media_voti[studente]=media
           
    context = { 
        'media_voti' : media_voti
    }
    return render(request, 'voti/media_voti.html', context)


# voti massimo e minimo, le materie in cui si sono registrati e gli studenti che li hanno ottenuti
def voto_max_min(request):
    
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    voto_max = 0
    voto_min = 11

    #trovo minimo e massimo
    for studente, materie in voti.items():
        for materia, voto, assenze in materie:
            if(voto>voto_max):
                voto_max=voto
            if(voto_min>voto):
                voto_min=voto

    studenti_max=[]
    studenti_min=[]
    materie_max=[]
    materie_min=[]

    for studente, materie in voti.items():
        for materia, voto, assenze in materie:
            if(voto_max==voto):
                studenti_max.append(studente)
                materie_max.append(materia)
            if(voto_min==voto):
                studenti_min.append(studente)
                materie_min.append(materia)

    max={
        'voto': voto_max,
        'studenti': studenti_max,
        'materie' : materie_max
    }
    min={
        'voto': voto_min,
        'studenti': studenti_min,
        'materie' : materie_min
    }

    context = {
        'min' : min,
        'max' : max
    }
    return render(request, 'voti/voto_max_min.html', context)