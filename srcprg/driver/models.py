from django.db import models


class Driver(models.Model):
    nome = models.CharField(max_length=50)
    data_nasc = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    cnh = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
