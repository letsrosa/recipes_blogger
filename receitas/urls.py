from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('receita/<int:id>/', views.receita_detail, name='receita_detail'),
    path('pesquisar/', views.pesquisar_receitas, name='pesquisar_receitas'), # <--- nova rota
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('contato/', views.contato, name='contato'),
    path('sucesso/', views.sucesso, name='sucesso'), # Rota para página de sucesso
]

