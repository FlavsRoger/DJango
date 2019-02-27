from django.db import models

# Create your models here.
              #Para trazer todas as ferramentas da classe model para o model.
class Pergunta(models.Model):
    texto = models.CharField()
    data = models.DateField()


class Alternativa(models.Model):
    texto = model.CharField()
    votos = model.IntegerField()