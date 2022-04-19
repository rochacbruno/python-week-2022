# python-week-2022
Template Para a Python Week 2002 - 25 a 29 de Abril na Linux Tips

## Instruções

Este repositório é um template de um projeto Python minimo  
O programa se chama `beerlog` e está organizado com pastas 
e módulos, porém a maioria dos arquivos encontra-se vazio.

A apartir deste template você poderá acompanhar as lives  
da Python week e programar junto com o Bruno e o Jeferson.

## Preparando o ambiente

- Você pode rodar localmente em seu computador desde que tenha o Python 3.8+
- Você pode rodar no [https://replit.com/](https://replit.com/) diretamente no browser
- Você pode rodar no [https://gitpod.io](https://gitpod.io)
- Ou qualquer plataforma que permita executar Python 3.8

## Requisitos

Este template utiliza o gerenciador de pacotes **poetry**

### Se estiver rodando no Linux no seu ambiente local

`execute o comando abaixo para instalar o Poetry no Linux`
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
### Ou em outros ambientes (incluindo o gitpod)

`Em outros ambientes pode instalar com `
```bash
pip install --user poetry
```

>  No replit.com o poetry já está disponível

## Instalando o ambiente

```bash
poetry install
poetry shell
beerlog
```

Se apareceu `Hello from beerlog` então está tudo certo.
