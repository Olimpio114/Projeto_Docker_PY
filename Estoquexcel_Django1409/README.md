
Estoque Django

=================================================================================
Projeto de exemplo utilizando **Python**, 
=================================================================================


## Tecnologias Utilizadas ##

- Python (gerenciado com pyenv)
- Virtualenv (venv)

---

## Pré-requisitos

- Python instalado (recomenda-se usar pyenv)
- - Git

---

## Configuração do Ambiente Python


## Como rodar seu projeto Django:

source venv/bin/activate

Isso é uma boa prática para manter as dependências do seu projeto isoladas.

Agora, execute o comando para iniciar o servidor de desenvolvimento do Django:
Bash
##    


Se você tiver o python3 como seu interpretador principal, talvez precise usar:
Bash

  ##  python3 manage.py runserver

    Após executar o comando, você verá uma mensagem no seu terminal, indicando que o servidor está rodando em um endereço como 
    
  ## http://127.0.0.1:8000/
     
    Basta copiar e colar esse endereço no seu navegador para ver o projeto em ação.

Algumas dicas extras:

    Se você quiser que o servidor seja acessível de outros dispositivos na sua rede, você pode rodá-lo com a opção 0.0.0.0:
    python manage.py runserver 0.0.0.0:8000

    Caso tenha problemas com as dependências do projeto, certifique-se de que todas estão instaladas executando:
    ## pip install -r requirements.txt


    python manage.py runserver 8001
python manage.py runserver 
python manage.py runserver 8001
python3 -m venv venv
source venv/bin/activate
deactivate


python manage.py makemigrations core
python manage.py migrate
============================
Primeiro, crie uma pasta para guardar o arquivo da fixture. No terminal, dentro da pasta core, execute o comando:

Bash

mkdir core/fixtures
Agora, use o comando do Django dumpdata para criar a fixture. Este comando vai extrair todos os dados dos seus modelos (Estoque e Produto) e salvar no arquivo que criamos.

Bash

python manage.py dumpdata core --indent 2 > core/fixtures/initial_data.json
O comando dumpdata lê o seu banco de dados, e o > core/fixtures/initial_data.json direciona a saída para o arquivo que você criou. O parâmetro --indent 2 deixa o arquivo mais fácil de ler.

Depois de rodar o comando, você verá um novo arquivo initial_data.json dentro da pasta core/fixtures. Você pode abrir este arquivo e ver todos os seus estoques e produtos em formato de texto.

Carregar o Estoque em Outra Máquina
Agora, quando você for para uma nova máquina, o processo será o seguinte:

Copie toda a pasta do projeto (com o arquivo initial_data.json dentro).

Instale as dependências com pip install -r requirements.txt (se você tem um arquivo de requisitos).

Crie as tabelas do banco de dados na nova máquina:

Bash

python manage.py makemigrations core
python manage.py migrate
Por fim, use o comando loaddata para carregar os dados da sua fixture:

Bash

python manage.py loaddata core/fixtures/initial_data.json
Pronto! Seu projeto e seus dados estarão intactos e prontos para serem usados na nova máquina.

Você quer tentar criar sua primeira fixture agora?