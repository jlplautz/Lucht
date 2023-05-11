from django.db import models

from srcprg.driver.models import Driver
from srcprg.truck.models import Truck


class Freight(models.Model):
    choices_pedagio = (('SP', 'Sem_parar'), ('DN', 'Dinheiro'))
    choices_frete = (('PG', 'Pago'), ('FS', 'Falta_Saldo'))
    contrato = models.CharField(max_length=15)
    cod_operacao = models.CharField(max_length=15)
    data = models.DateField(auto_now_add=True)
    caminhao = models.ForeignKey(Truck, on_delete=models.DO_NOTHING)
    motorista = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    origem = models.CharField(max_length=30, verbose_name='Origem')
    Km_origem = models.IntegerField
    destino = models.CharField(max_length=30, verbose_name='Destino')
    Km_destino = models.IntegerField
    pedagio_pgto = models.CharField(
        max_length=2,
        choices=choices_pedagio,
        default='SP',
    )
    pedagio_valor = models.CharField(max_length=10)
    adiantamento_valor = models.CharField(max_length=10)
    saldo_valor = models.CharField(max_length=10)
    frete_status = models.CharField(
        max_length=2, choices=choices_frete, default='FS'
    )

    def __str__(self):
        return self.origem
