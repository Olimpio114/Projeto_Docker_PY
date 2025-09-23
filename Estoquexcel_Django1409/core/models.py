# core/models.py

from django.db import models


class Estoque(models.Model):
    """
    Representa um estoque único.
    Cada estoque terá um nome e uma data de criação.
    """
    nome = models.CharField(
        max_length=100,
        unique=True,
        help_text="Nome do estoque (ex: 'Cozinha', 'Garagem')."
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        help_text="Data e hora em que o estoque foi criado."
    )

    def __str__(self):
        """Retorna o nome do estoque."""
        return self.nome

class Produto(models.Model):
    """
    Representa um produto dentro de um estoque.
    Cada produto pertence a um Estoque (chave estrangeira).
    """
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='produtos',
        help_text="O estoque ao qual este produto pertence."
    )
    nome = models.CharField(
        max_length=200,
        help_text="Nome do produto (ex: 'Arroz', 'Sabão')."
    )
    quantidade = models.PositiveIntegerField(
        help_text="Quantidade do produto em estoque."
    )
    preco_estimado = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Preço estimado do produto."
    )

    def __str__(self):
        """Retorna o nome do produto e o estoque a que ele pertence."""
        return f"{self.nome} ({self.estoque.nome})"
    

class Estoque(models.Model):
    nome = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Adicione o novo modelo para os produtos aqui
class Produto(models.Model):
    # O "ForeignKey" é o que conecta um Produto a um Estoque
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)
    preco_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome