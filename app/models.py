from django.db import models

class ApiModel(models.Model):
    Sensor = models.BooleanField(default=False)
    Botao = models.BooleanField(default=False)
    LigaRobo = models.BooleanField(default=False)
    ResetContador = models.BooleanField(default=False)
    Valor_Contagem = models.IntegerField(default=0)

    def __str__(self):
            return "ApiModel object"


