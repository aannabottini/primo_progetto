import requests
import spotipy
from django.shortcuts import render
from spotipy.oauth2 import SpotifyOAuth

def indexApi(request):
    return render(request, "api/index.html")

def todos_view(request):
    # Effettua la richiesta HTTP
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos/')
        if response.status_code == 200:
            lista_todos = response.json()
            messaggio_errore = None
        else:
            lista_todos = []
            messaggio_errore = "Errore nel recupero dei dati. Codice di stato: " + str(response.status_code)
    except Exception as e:
        lista_todos = []
        messaggio_errore = "Errore nella connessione all'API: " + str(e)

    # Passa i dati al template
    return render(request, 'todos.html', {
        'todos': lista_todos,
        'errore': messaggio_errore
    })


def spotify_view(request):
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="9f7aead6289b490082175d8e76ad8193",
        client_secret="cce13e49a56a4bc48f4d40671f3d9c12",
        redirect_uri="http://127.0.0.1:8000/callback/",
        scope=["user-library-read"],
        cache_path=".cache"
    ))

    tracce_salvate = []
    messaggio_errore = None

    try:
        results = sp.current_user_saved_tracks()
        
        # Invece di fare print nel terminale, costruiamo una lista di dizionari 
        # contenente i dati che ci interessano, così da passarli all'HTML
        for item in results['items']:
            track = item['track']
            tracce_salvate.append({
                'titolo': track['name'],
                'artista': track['artists'][0]['name']
            })
            
    except Exception as e:
        messaggio_errore = f"Errore di connessione a Spotify: {str(e)}"

    return render(request, 'api/spotify.html', {
        'tracce': tracce_salvate,
        'messaggio_errore': messaggio_errore
    })