# Usa uma imagem base oficial do Python, versão 3.10, no modo "slim"
FROM python:3.13.7-slim

# Define variáveis de ambiente para o Python
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Adiciona a pasta `src` ao caminho de busca de módulos do Python
ENV PYTHONPATH=/app/src

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da sua aplicação para o diretório de trabalho
COPY . .

# Expõe a porta que a aplicação vai usar
EXPOSE 8000

# Define o comando para rodar o manage.py da raiz do projeto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]