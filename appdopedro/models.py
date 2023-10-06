from django.db import models

# Create your models here.
class Filmes(models.Model):
    titulo = models.CharField(max_length=50)
    diretor = models.CharField(max_length=70)
    genero = models.CharField(max_length=20)
    lancamento = models.DateField(max_length=50)

class Jogos(models.Model):
    JOGABILIDADE = [("L", "Local"),
                    ("O", "Online"),
                    ("A", "Ambos")]
    GENERO = [("S", "Shooter"),
              ("E", "Esporte"),
              ("H", "História"),
              ("A", "Arcade")]
    titulo = models.CharField(max_length=50)
    empresa = models.CharField(max_length=70)
    jogabilidade = models.CharField(max_length=1, choices=JOGABILIDADE)
    genero = models.CharField(max_length=4, choices=GENERO)
    lancamento = models.DateField(max_length=50)