# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estoques/', views.listar_estoques, name='listar_estoques'),
    path('estoques/criar/', views.criar_estoque, name='criar_estoque'),
    path('estoques/apagar/<int:estoque_id>/', views.apagar_estoque, name='apagar_estoque'),
    path('relatorio-geral/', views.gerar_relatorio_geral, name='gerar_relatorio_geral'),
    path('estoques/<int:estoque_id>/produtos/', views.gerenciar_produtos, name='gerenciar_produtos'),
    path('estoques/<int:estoque_id>/produtos/', views.gerenciar_produtos, name='gerenciar_produtos'),
    path('estoques/<int:estoque_id>/produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('estoques/<int:estoque_id>/produtos/', views.gerenciar_produtos, name='gerenciar_produtos'),
    path('estoques/<int:estoque_id>/produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/<int:produto_id>/<str:acao>/', views.modificar_quantidade_produto, name='modificar_quantidade_produto'),
    path('produtos/apagar/<int:produto_id>/', views.apagar_produto, name='apagar_produto'),
    path('relatorio-geral/', views.gerar_relatorio_geral, name='gerar_relatorio_geral'),
    path('exportar-relatorio/', views.exportar_relatorio, name='exportar_relatorio'),




]