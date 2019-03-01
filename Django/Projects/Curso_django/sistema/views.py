# 1º a biblioteca primaria e depois a secundaria..
from django.http import HttpResponse

# criaremos um FUNÇÂO chamada index(request) q tem que fazer


def index(request):
    return HttpResponse('<h1> Pagina Inicial!</h1>')
