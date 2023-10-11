# Documentação do Projeto de Gerenciamento de Álbuns e Músicas

## Visão Geral
Este projeto foi criado com o objetivo de permitir que os usuários cadastrem seus álbuns e músicas. Foram implementadas diferentes permissões de acesso para distinguir entre superusuários e usuários regulares, limitando as funcionalidades com base no tipo de usuário. O projeto foi desenvolvido utilizando Python, o framework Django e o banco de dados PostgreSQL.

## Funcionalidades Principais
O projeto incluiu as seguintes funcionalidades principais:

1. **Autenticação de Usuários**: Os usuários podiam se cadastrar, fazer login e gerenciar suas contas.

2. **Gestão de Álbuns**: Os usuários podiam adicionar, editar e remover álbuns da sua coleção pessoal. Cada álbum incluía informações como título, artista, data de lançamento e capa.

3. **Gestão de Músicas**: Além de álbuns, os usuários podiam cadastrar suas músicas. Cada música estava associada a um álbum e continha informações como título e duração.

4. **Controle de Permissões**: O projeto implementou diferentes níveis de permissão para usuários, distinguindo entre superusuários e usuários regulares. O acesso a determinadas funcionalidades era restrito com base nas permissões do usuário.

## Executando o Projeto
Para executar o projeto, siga estas etapas:

1. Clone o repositório para o seu ambiente local:
   ```shell
   git clone https://github.com/seuusuario/seuprojeto.git
   ```

2. Navegue até o diretório do projeto:
   ```shell
   cd seuprojeto
   ```

3. Crie um ambiente virtual Python (recomendado) e ative-o:
   ```shell
   python -m venv venv
   source venv/bin/activate
   ```

4. Instale as dependências do projeto usando o `requirements.txt`:
   ```shell
   pip install -r requirements.txt
   ```

5. Configure as variáveis de ambiente e defina as configurações do banco de dados no arquivo `settings.py`.

6. Aplique as migrações do banco de dados:
   ```shell
   python manage.py migrate
   ```

7. Crie um superusuário (admin) para acessar as funcionalidades de superusuário:
   ```shell
   python manage.py createsuperuser
   ```

8. Inicie o servidor de desenvolvimento:
   ```shell
   python manage.py runserver
   ```

9. Acesse a aplicação no seu navegador em [http://localhost:8000](http://localhost:8000).

Certifique-se de personalizar a documentação do seu projeto com informações adicionais, como modelos de banco de dados, endpoints de API, instruções de uso e qualquer outra informação relevante para futuros desenvolvedores que possam colaborar com o projeto.
