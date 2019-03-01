para começar um projeto temos que ir para pasta e dar o comando inicial
 Django-admin startproject Curso_django , sendo que "Curso_django" é o nome do diretorio.


 dentro da pasta criada, o Django criou os arquivo de  inicialização.

 2-Feito isto dentro do diretorio criado daremos o 1º comando.

 python manage.py runserver

 Isto vai abrir o arquivo principal no servidor.


 Vamos baixar e instalar o XAMPP que é uma banco de dados APACHE, baixe a ultima versão

 3- vamos instalar uma aplicação para organizar os arquivos
 como se fosse um instrutura em MVC, para instalar esta instrutura, existe um comando
 que podemos usar dentro do terminal, sem precisar criar pastas, etc.

 python manage.py startapp sistema   // onde "Sistema é o diretorio criado"


 OBs.: Lembrando que  inciamos nosso servidor com o comando:
 "Django-admin startproject Curso_django" , ele continua rodando, enquanto ele
 estiver inicializado conseguiremos ver a nossa tela no localhost:8000, para párar o
 servidor usamos o CTRL+C

 3-a Feito isto ele , ele criou uma pasta chamada SISTEMA e já colocou os arquivo dentro
 e dentro da Pasta SISTEMA, ele criou um arq. administrador e VIEW e TESTE e  outros que serão explicados:
 exemplo se formos no:
  localhost:8000/admin "ele mostrará uma pagina já criada para login do administrador feita pelo comando"
  se tentarmos usar outro caminho ele vai dar erro, visto que não existe path na URL deste arquivo, tudo começa com ADMIN.

  "localhost:8000/tests"
  Using the URLconf defined in Curso_django.urls, Django tried these URL patterns, in this order:

  admin/
  The current path, tests, didn't match any of these.

  4- A primeira coisa que temos que fazer é corrigir TODOS os caminhos de URL das paginas criadas
  vamos fazer isto agora:

  4-1 Mas primeiro temos que inicializar o serivor XAMPP e temos que starta os 2 serviços principais deles
   o APACHe e o MYSQL, ele tem que ficarem "VERDES" caso contrario algum programa  pode está proibindo
   o servidor de startar:
   Podemos clicar para fechar que ele ficará rodando em 2º plano, na barra de tarefas.

   Obs: ele só vai abrir as pagina no servidor, se ACERTAMOS os path dentro de URLs.

   4-2 Vamos abrir nosso arquivo de URL na IDE, e lá fazer as alteração.
   lembrando que temos 2 Arq. de URL, 1 para Paginas EXTERNAS já criado e outro para Paginas INTERNAS,
   que iremos criar dentro  da pasta SISTEMAS um arquivo do URLSINTERNA.PY ou qualquer nome.

   4-3 vamos copiar umas linha do nosso URL externo e colarmos no nosso URL interno
   e fazermos algumas alterações.

   segue o que copiaremos:
   "
    from django.urls import path
   "
   Mas temos que MUDAR  o caminho apontando agora para nossa pasta onde criamos a URL_INTERNA:

from django.conf.urls import url

   # Aqui importamos da RAIZ"." Todas as informações de vistas, para o arquivo VIEWS
from . import views

   #Vamos copiar tb a extrutura para trabalhar com URLs e mudaremos tb ela:

   "urlpatterns = [
    path('admin/', admin.site.urls),
   ]
   "
   E ficará assim mudada uma URL para INDEX, criando uma associção para RAIZ da pasta usando os CARACTERES abaixo.
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
   # Onde mudamos de:
    URL  #mudamos de path para URL
    r'^$' #usamos este especiais para irmos para RAIZ
    views.index #apontamos para o arquivo VIEWS
    .index #temos que criar este arquivo INDEX
    name='index' # eu dou um nome ao meu arquivo, neste caso INDEX



















