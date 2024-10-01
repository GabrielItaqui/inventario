# views.py
from django.shortcuts import render

salas = [
    {'nome': 'Sala 1B', 'bloco': 'B'},
    {'nome': 'Sala 2B', 'bloco': 'B'},
    {'nome': 'Sala 3B', 'bloco': 'B'},
    {'nome': 'Sala 4B', 'bloco': 'B'},
    {'nome': 'Sala 5B', 'bloco': 'B'},
    {'nome': 'Sala 6B', 'bloco': 'B'},
    {'nome': 'Sala 7B', 'bloco': 'B'},
    {'nome': 'Sala 8B', 'bloco': 'B'},
    {'nome': 'Sala 9B', 'bloco': 'B'},
    {'nome': 'Sala 10B', 'bloco': 'B'},
    {'nome': 'Sala 11B', 'bloco': 'B'},
    {'nome': 'Sala 12B', 'bloco': 'B'},
    {'nome': 'Sala 13B', 'bloco': 'B'},
    {'nome': 'Sala 14B', 'bloco': 'B'},
    {'nome': 'Sala 15B', 'bloco': 'B'},
    {'nome': 'Sala 16B', 'bloco': 'B'},
    {'nome': 'Sala 17B', 'bloco': 'B'},
    {'nome': 'Sala 18B', 'bloco': 'B'},
    {'nome': 'Sala 19B', 'bloco': 'B'},
    {'nome': 'Sala 20B', 'bloco': 'B'},
]

def index(request):
    return render(request, 'main/index.html', {"salas": salas})