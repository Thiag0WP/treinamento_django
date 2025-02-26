from django.contrib import admin
from .models import Veiculo, Movimentacao
from datetime import timedelta

class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ['veiculos', 'entrada', 'saida', 'tempo_permanencia']

    def tempo_permanencia(self, obj):
        if obj.saida and obj.entrada:
            return obj.saida - obj.entrada
        return timedelta(0)
    tempo_permanencia.short_description = 'Tempo de permanência'


admin.site.register(Veiculo)


admin.site.register(Movimentacao, MovimentacaoAdmin)