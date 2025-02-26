from django.db import models

# Create your models here.

class Veiculo(models.Model):
    placa = models.CharField(max_length=7, help_text='Placa do veículo', verbose_name='Placa', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.placa
    
class Movimentacao(models.Model):
    veiculos = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING, verbose_name='Veículo', related_name='Movimentacoes')
    entrada = models.DateTimeField(auto_now_add=True, verbose_name='Entrada')
    saida = models.DateTimeField(null=True, blank=True, verbose_name='Saída')


    def __str__(self):
        return f"{self.veiculos.placa} - {self.entrada} - {self.saida}"