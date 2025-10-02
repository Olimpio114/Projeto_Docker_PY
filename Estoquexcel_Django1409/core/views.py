# Create your views here.
# core/views.py
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
import pandas as pd
from .models import Estoque, Produto
from .forms import ProdutoForm
from django.db.models import Sum 


def home(request):
    """
    Renderiza a página inicial com as opções de menu.
    """
    return render(request, 'core/home.html')

def listar_estoques(request):
    """
    Busca todos os estoques do banco de dados e os exibe.
    """
    estoques = Estoque.objects.all()
    context = {
        'estoques': estoques,
    }
    return render(request, 'core/listar_estoques.html', context)

def criar_estoque(request):
    """
    Renderiza o formulário para criar um novo estoque.
    Se a requisição for POST, salva o novo estoque no banco de dados.
    """
    if request.method == 'POST':
        nome_estoque = request.POST.get('nome_estoque')
        if nome_estoque:
            Estoque.objects.create(nome=nome_estoque)
            return redirect('listar_estoques')

    return render(request, 'core/criar_estoque.html')

def apagar_estoque(request, estoque_id):
    """
    Busca e apaga um estoque específico do banco de dados.
    """
    estoque = get_object_or_404(Estoque, pk=estoque_id)
    estoque.delete()
    return redirect('listar_estoques')








def gerar_relatorio_geral(request):
    estoques = Estoque.objects.all().order_by('nome')
    relatorio_texto = ""

    if estoques:
        relatorio_texto += "RELATÓRIO GERAL DE ESTOQUES\n\n"
        for estoque in estoques:
            relatorio_texto += f"----------------------------------------\n"
            relatorio_texto += f"Estoque: {estoque.nome}\n"
            
            produtos = estoque.produto_set.all().order_by('nome')
            
            if produtos:
                total_estoque = produtos.aggregate(total_valor=Sum('preco_estimado'))['total_valor'] or 0
                relatorio_texto += f"Valor total do Estoque: R$ {total_estoque:.2f}\n"
                relatorio_texto += "----------------------------------------\n"
                relatorio_texto += "Produtos:\n"
                
                for produto in produtos:
                    relatorio_texto += f"  - {produto.nome}: {produto.quantidade} unid. | R$ {produto.preco_estimado:.2f} | Última Atualização: {produto.data_ultima_atualizacao.strftime('%d/%m/%Y %H:%M')}\n"
            else:
                relatorio_texto += "Este estoque não contém produtos.\n"
        
    else:
        relatorio_texto = "Não existem estoques para gerar relatório."

    contexto = {'conteudo_txt': relatorio_texto}
    return render(request, 'core/relatorio_geral.html', contexto)
def gerenciar_produtos(request, estoque_id):
    estoque = get_object_or_404(Estoque, id=estoque_id)
    produtos = estoque.produto_set.all()

    context = {
        'estoque': estoque,
        'produtos': produtos
    }
    return render(request, 'core/gerenciar_produtos.html', context)

def gerenciar_produtos(request, estoque_id):
    estoque = get_object_or_404(Estoque, id=estoque_id)
    produtos = estoque.produto_set.all()
    form = ProdutoForm() # Instanciar o formulário para a página

    context = {
        'estoque': estoque,
        'produtos': produtos,
        'form': form # Passar o formulário para o template
    }
    return render(request, 'core/gerenciar_produtos.html', context)


def adicionar_produto(request, estoque_id):
    if request.method == 'POST':
        estoque = get_object_or_404(Estoque, id=estoque_id)
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.estoque = estoque
            produto.save()
            return redirect('gerenciar_produtos', estoque_id=estoque.id)
    return redirect('gerenciar_produtos', estoque_id=estoque_id)
def modificar_quantidade_produto(request, produto_id, acao):
    produto = get_object_or_404(Produto, id=produto_id)

    if acao == 'aumentar':
        produto.quantidade += 1
    elif acao == 'diminuir' and produto.quantidade > 0:
        produto.quantidade -= 1
    
    produto.save()
    return redirect('gerenciar_produtos', estoque_id=produto.estoque.id)
def apagar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    estoque_id = produto.estoque.id
    produto.delete()
    return redirect('gerenciar_produtos', estoque_id=estoque_id)








def exportar_relatorio(request):
    estoques = Estoque.objects.all().order_by('nome')

    # 1. Gerar o Relatório de Texto
    relatorio_texto = ""
    if estoques:
        relatorio_texto += "RELATÓRIO GERAL DE ESTOQUES\n\n"
        for estoque in estoques:
            relatorio_texto += f"----------------------------------------\n"
            relatorio_texto += f"Estoque: {estoque.nome}\n"
            produtos = estoque.produto_set.all().order_by('nome')
            
            if produtos:
                total_estoque = produtos.aggregate(total_valor=Sum('preco_estimado'))['total_valor'] or 0
                relatorio_texto += f"Valor total do Estoque: R$ {total_estoque:.2f}\n"
                relatorio_texto += "----------------------------------------\n"
                relatorio_texto += "Produtos:\n"
                
                for produto in produtos:
                    relatorio_texto += f"  - {produto.nome}: {produto.quantidade} unid. | R$ {produto.preco_estimado:.2f} | Última Atualização: {produto.data_ultima_atualizacao.strftime('%d/%m/%Y %H:%M')}\n"
            else:
                relatorio_texto += "Este estoque não contém produtos.\n"
    else:
        relatorio_texto = "Não existem estoques para gerar relatório."

    # 2. Gerar o Relatório em Excel (DataFrame)
    dados_excel = []
    for estoque in estoques:
        produtos = estoque.produto_set.all()
        for produto in produtos:
            dados_excel.append({
                'Estoque': estoque.nome,
                'Produto': produto.nome,
                'Quantidade': produto.quantidade,
                'Preço Estimado': produto.preco_estimado,
                'Data de Atualizacao': produto.data_ultima_atualizacao.strftime('%d/%m/%Y %H:%M')
            })
    
    df = pd.DataFrame(dados_excel)
    
    # 3. Salvar os arquivos
    output_dir = os.path.join(settings.BASE_DIR, 'data', 'output')
    os.makedirs(output_dir, exist_ok=True) # Cria a pasta se ela não existir
    
    # Salvar arquivo de texto
    with open(os.path.join(output_dir, 'relatorio_estoques.txt'), 'w', encoding='utf-8') as f:
        f.write(relatorio_texto)

    # Salvar arquivo Excel
    if not df.empty:
        df.to_excel(os.path.join(output_dir, 'relatorio_estoques.xlsx'), index=False)
    
    return redirect('gerar_relatorio_geral')