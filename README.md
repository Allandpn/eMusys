# eMusys
#### Video Demo: <url>
#### Description: Este resposítório contém os aquivos do Final Project do curso CS50’s Introduction to Computer Science da Harvard University. Trata-se de um sistema de gestão de uma escola de música, com controle de acervo e gestão de empréstimos de instrumentos para os alunos. 


### Requisitos
Necessário instalação de Python e do framework Flask.
`https://flask.palletsprojects.com/en/3.0.x/quickstart/`


### Instalação
1. Crie um ambiente virtual para a aplicação
2. Execute o comando `pip install -r requierements.txt` para instalar as dependências
3. Execute `python run.py` para iniciar o sistema.
 

### Estrutura
A estrutura do sistema ficou organizada nas seguintes Blueprint:
* main
  - Rota de início da aplicação. Direciona à página `dashboard.html` com um resumo dos dados do sistema.
* user
  - Trata das requisições de Login e Registro de usuário. Inclui também a página para recuperação de senha com link enviado por email
* admin
  - Área da administração da escola. Permite a consulta, cadastro, atualização e exclusão de Unidades, Turmas e Colaboradores
* aluno
  - Área com as informações sobre os alunos. Permite a consulta, cadastro, atualização e exclusão de alunos
* acervo
  - Área com as insformaçòes sobre os instrumentos. Inclui a consulta, cadastro, atualização e exclusão de instrumentos e a gestão de empréstimos aos alunos
* errors
  - Trata os erros 404, 403, 5000 direcionando a uma página de erro correspondente

  Cada Blueprint possui um arquivo
  * `__init__.py` - defini como package
  * `forms.py` - contém os forumlários Flask_form
  * `utils.py` - funcões de suporte para as rotas e formulários
  * `routes.py` - rotas para a aplicação
 
  Para o Banco de Dados foi escolhido o SQLite, o qual está definido em `instance/dev.db`. As versões do banco de dados utilizadas durante o desenvolvimento estão na pasta `migrations/versions`


### Autores
- Allan Nascimento

### Agradecimentos
- Esse sistema se baseia em um sistema que também foi apresentado na disciplina do curso de Sistemas de Informação da PUC Minas, a quem deixo meus agradecimentos.
- Um agredecimento especial ao prof. David J. Malan e sua equipe, que proporcionou um curso formidável de introdução à computação. 

### Licença
Este projeto é licenciado sob a [MIT License](https://github.com/Allandpn/eMusys/blob/main/LICENSE).
