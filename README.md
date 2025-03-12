# gerenciadorCadastros

### Gerenciador de cadastro de profissionais e suas expertises

 Programa que tem como fim, efetuar o cadastro de profissionais
 da area medica e suas expertises


## Alguns comandos uteis para a configuração do ambiente

 py -m venv my-venv                  -- cria ambiente virtual

 pip install flask                   -- instala o flask

 my-venv\Scripts\activate            -- ativa ambiente virtual

 deactivate                          -- desativa ambiente virtual

 set Flask_APP=app                   -- indiaca ao flask qual app sera carregado no servidor web

 pip install mysql-connector-python  -- instala o conector para o banco de dados

 Flask run                           -- executa flask


## Hierarquia dos arquivos

project/
│
├── templates/                              # definições da visao do aplicativo
│   ├── alterarCadastro.html
│   ├── cadastrarEspecialidades.html
│   ├── cadastrarProfissionais.html
│   ├── consultarDisponibilidade.html
│   ├── editarProfissional.html
│   ├── listarProfissionais.html
│   ├── operacao_sucesso.html
│   ├── resultadoDisponibilidade.html
│   └── sistema.html
│
├── modelos/                                 # Definições dos modelos de dados
|   ├── disponibilidade.py
│   ├── profissionais.py
│   └── especialidades.py
│
├── servicos/                                 # Definições dos modelos de dados
│   └── sistema_facade.py
|
├── controladores/                            # camada de controle superior
|   ├── consultar_disponibilidade.py
│   ├── cadastros.py
│   └── update_profissional.py
│
├── testes/  
|   ├── test_real.py
|   └── test_simulado.py
|
└── app.py                                  # Arquivo principal que executa o aplicativo Flask

## Dependencias

 SGBD Mysql
 Interpretador python
 mysql-connector-python
 Flask
 módulo unittest

  ## Observação
 Alem de cumprir todas as dependencias é fundamental atualizar a 
 configuração do banco de dados nos arquivos do diretorio models 
 com os dados do seu banco.

 Exemplo:
 
    "host": "Meu host",              
    "user": "Meu nome de usuario",         
    "password": "Minha senha",            
    "database": "sistema_profissionais"       
