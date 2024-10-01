from django.db import models

class Salas(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    bloco = models.CharField(max_length=100, null=False, blank=False)
    projetorMarca = models.CharField(max_length=100, null=False, blank=False)
    arCondicionadoMarca = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Salas [nome={self.nome}]"