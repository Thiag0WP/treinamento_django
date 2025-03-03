# Generated by Django 5.1.6 on 2025-02-26 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='entrada',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Entrada'),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='saida',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Saída'),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='veiculos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Movimentacoes', to='base.veiculo', verbose_name='Veículo'),
        ),
    ]
