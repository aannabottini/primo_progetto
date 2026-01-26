from django.db import models

# Create your models here.
class Giornalista(models.Model):
    nome=models.CharField(max_length=20) #Stringhe di lunghezza massima 20
    cognome=models.CharField(max_length=20)
    anno_nascita=models.DateField(blank=True)
    #crea un id auto_increment 'nascosto' se non specificato
    
    def __str__(self):
        return self.nome + " " + self.cognome
    class Meta:
        verbose_name = 'Giornalista'
        verbose_name_plural = 'Giornalisti'

class Articolo(models.Model):
    visualizzazioni=models.IntegerField(default=0, blank=True)
    data_articolo=models.DateField(blank=True)
    #data_articolo=models.DateField(auto_now=True, blank=True)
    titolo=models.CharField(max_length=100) #Stringhe di lunghezza massima 100
    contenuto=models.TextField()
    giornalista=models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name = 'Articolo'
        verbose_name_plural = 'Articoli'