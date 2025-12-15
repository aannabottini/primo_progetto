from django.db import models

# Create your models here.
class Giornalista(models.Model):
    nome=models.CharField(max_length=20) #Stringhe di lunghezza massima 20
    cognome=models.CharField(max_length=20)
    #crea un id auto_increment 'nascosto' se non specificato
    
    def __str__(self):
        return self.nome + " " + self.cognome

class Articolo(models.Model):
    titolo=models.CharField(max_length=100) #Stringhe di lunghezza massima 100
    contenuto=models.TextField()
    giornalista=models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    def __str__(self):
        return self.titolo
    