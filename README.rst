Documentos-Projetos_Docker_PY
==================================================================================== 
Projeto de exemplo utilizando Python , Docker e pyenv para gerenciamento de versões.
===================================================================================
Tecnologias Utilizadas
Python (gerenciado com pyenv)
Docker
Docker Compose
Virtualenv (venv)
Pré-requisitos
Python instalado (recomenda-se usar pyenv)
Docker
Docker Compose
Git
================================================================================
Configuração do Ambiente Python
Instale a versão do Python desejada usando pyenv :
pyenv install 3.12.2
pyenv local 3.12.2
==============================================================================
Reconstrua a imagem Docker 
docker build -t minha-primeira-imagem .

Execute o contêiner   
docker run -p 8000:8000 minha-primeira-imagem
sudo usermod -aG docker "nomeusuario"
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Executando o Docker Compose
Acesse a aplicação no navegador:
Abra seu navegador e digite o seguinte endereço: 
http://localhost:8000.

Pare os serviços:
Quando você terminar, volte para o terminal e pressione 
Ctrl + C.

Para reativar os serviços:
docker compose up

=============================================================================
1. Rodar Migrações e Criar um Superusuário: Como o banco de dados está vazio, 
você precisará aplicar as migrações do Django e criar um usuário administrador 
para acessar o painel de administração.

2. Conectar-se ao Banco de Dados: Acessar o banco de dados do seu computador 
local, usando uma ferramenta como o DBeaver ou psql, para gerenciar os dados
 diretamente.

3. Configurar um Servidor de Produção: Mudar do servidor de desenvolvimento 
do Django para um servidor de produção como o Gunicorn para se preparar para 
o deploy.
==============================================================================
Para adquirir secret-key
Execute o comando shell 
PYTHONPATH=./src python manage.py shell

Gerar a chave: Dentro do console do Django, execute as seguintes linhas:
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
============================================================================
1. Fazer as Migrações do Banco de Dados: Aplicar as tabelas do Django no seu banco 
de dados PostgreSQL.
docker compose up

2. Criar uma Aplicação Django: Iniciar a criação de uma nova aplicação (startapp) 
para começar a construir as funcionalidades do seu projeto.
docker compose exec web python manage.py migrate
3. Criar um Superusuário: Criar uma conta de administrador para acessar o painel 
de administração do Django.
=================================================================================

Ver os contêineres em execução
Este é o comando mais comum para verificar se algo está ativo no Docker.

docker ps

Verificar os logs do contêiner
O servidor Django já imprime os logs diretamente no seu terminal, mas e se você tivesse 
rodado o contêiner em segundo plano? Você pode ver os logs de um contêiner específico com este comando:

docker logs <nome_do_seu_contêiner>
================================================================================
Como Criar uma POC com seu Projeto
----------------------------------
docker-compose exec web python manage.py startapp poc
================================================================================
<<<<<Rodar o programa na pasta raiz do projeto>>>> 
-------------------------------------------------
docker-compose up    >. rodar 
docker-compose up -d   >>rodar em segundo plano
docker-compose ps  >> verificar os contêiners

cole em uma página>>> http://0.0.0.0:8000/

Acessar a Segunda Tela (o Painel de Administração) >>>  http://localhost:8000/admin/
se não funcionar siga>>
depois abra um terminal diferente veja exemplo e rode o código:
olimpio@olimpio:~/Documentos/Projeto_DockerEstudo$ docker-compose exec web python manage.py migrate
===============================================================================
Como Criar uma POC com seu Projeto
docker-compose exec web python manage.py startapp poc

Para que uma POC seja eficaz, ela deve ser focada em uma única funcionalidade. 
Um ótimo exemplo é uma lista de tarefas simples (um "To-Do List").

Isso vai testar a capacidade do seu projeto de:

-Receber dados do usuário através de um formulário web.

-Salvar esses dados no banco de dados PostgreSQL.

-Ler esses dados do banco de dados e exibi-los em uma página web.

Com isso, você prova que seu sistema (Django, PostgreSQL, Docker) funciona em conjunto para um problema real.
================================================================================
A estrutura da tabela Task foi definida no arquivo poc/models.py

Os comandos de migração foram executados para traduzir o modelo de dados em uma tabela real no banco de dados PostgreSQL.

docker-compose exec web python manage.py makemigrations poc
docker-compose exec web python manage.py migrate


Configuração do Painel de Administração

Um superusuário foi criado para ter acesso ao painel de administração integrado do Django.
 Em seguida, a tabela Task foi registrada para ser gerenciada diretamente no painel.

docker-compose exec web python manage.py createsuperuser

Criação da Lógica da Aplicação (View)
A lógica para a aplicação de tarefas foi implementada no arquivo poc/views.py.
Mapeamento das URLs
As URLs foram configuradas para direcionar as requisições web para a view correta, tanto para 
a página principal da POC quanto para o painel de administração.

Desenvolvimento da Interface (Template)
O arquivo HTML (poc/templates/poc/task_list.html) foi criado para fornecer a interface de usuário,
 com um formulário para adicionar tarefas 
e uma lista para exibi-las.

=================
Demonstração da POC
Para demonstrar a aplicação funcional:

Inicie o ambiente: No terminal, execute docker-compose up -d para garantir que o projeto esteja rodando.

Acesse a POC: Abra o navegador e acesse a URL http://localhost:8000/.

Adicione uma tarefa: Use o formulário na página principal para adicionar uma nova tarefa. A página será recarregada, e a tarefa aparecerá na lista.

Acesse o painel de administração: Vá para http://localhost:8000/admin/ e faça login com o superusuário criado.