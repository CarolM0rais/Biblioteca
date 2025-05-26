from django.contrib import admin
from django.urls import path
from app.views import IndexView, LivrosView, CidadesView, AutoresView, EditorasView, LeitoresView, GenerosView
# from app.views import EmprestimoView  # descomente se for usar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('livros/', LivrosView.as_view(), name='livros'),
    # path('reserva/', EmprestimoView.as_view(), name='reserva'),  # descomente se criar Reserva
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('autor/', AutoresView.as_view(), name='autor'),
    path('editora/', EditorasView.as_view(), name='editora'),
    path('leitor/', LeitoresView.as_view(), name='leitor'),
    path('genero/', GenerosView.as_view(), name='genero'),
]
