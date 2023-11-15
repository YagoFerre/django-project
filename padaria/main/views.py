from django.shortcuts import render
from .models import Produto

def home(request):
    produto = Produto.objects.all()
    return render(request, 'index.html', {'produto': produto})

def carrinho(request):
    return render(request, 'carrinho.html')