# MEDICAR API
Projeto de sistema de agendamento de consultas medicas.  

Desenvolvido como desafio para vaga de desenvolvedor Intmed, mais informações do desafio [aqui](https://github.com/Intmed-Software/desafio).

Api desenvolvida com Django Rest Framework.

## Configurando o ambiente

```
  #cria o ambiente virtual
  python -m venv env
  
  #ativa o ambiente (Linux)
  source env/bin/activate
  #ativa o ambinente (Windows - Powershell)
  .\env\Scripts\activate
  
  #instale as dependências (Windows - Powershell)
  python -m pip install -r requirements.txt
  
  #instale as dependências (Linux)
  pip install -r requirements.txt
```

## Configurando o Banco de Dados

O projeto está configurado para utilizar banco de dados `mysql`.

No arquivo `medicarApi/settings.py` identifique a seção:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'medicar_db', #Nome do Banco
        'USER': 'yvens',  #Usuario
        'PASSWORD': 'root', #Senha
        'HOST': 'localhost', 
        'PORT': '3306',
    }
}
```
Insira suas configurações e salve.


## Executando o projeto

Após configurar o banco basta executar os seguintes comandos.

```
Rodando o projeto (Windows - Powershell)
  py .\manage.py makemigrations
  py .\manage.py migrate
  py .\manage.py runserver
  
Rodando o projeto (Linux)
  py manage.py makemigrations
  py manage.py migrate
  py manage.py runserver
  
```