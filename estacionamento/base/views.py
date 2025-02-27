from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.db.models import query
from .models import Movimentacao

def home(request):

    movimentacao = Movimentacao
    query = Movimentacao.objects.all()
    context = {
        'movimentacao' : movimentacao,
        'query' : query,
    }

    return render(request, 'home.html')

# Create your views here.
