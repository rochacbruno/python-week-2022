# python-week-2022
Template Para a Python Week 2002 - 25 a 29 de Abril na Linux Tips

## Instruções

Este repositório é um template de um projeto Python minimo  
O programa se chama `beerlog` e está organizado com pastas 
e módulos, porém a maioria dos arquivos encontra-se vazio.

A apartir deste template você poderá acompanhar as lives  
da Python week e programar junto com o Bruno e o Jeferson.

## Obtendo seu repositório

01. Faça login no github (cadastre-se gratuitamente caso ainda não tenha uma conta)
00. Crie um **fork** (cópia) deste repositório clicando em [fork](https://github.com/rochacbruno/python-week-2022/fork)
00. O seu repositório estará em https:// github.com / SEUNOME / python-week-2022
00. Copie a URL do seu repositório (você vai precisar depois)

## Preparando o ambiente

> **OBS** substitua `SEUNOME` pelo seu nome de usuário do github.

- Você pode rodar localmente em seu computador desde que tenha o Python 3.8+
    - Para rodar localmente faça o clone com `git clone https://github.com/SEUNOME/python-week-2022`
    - Acesse a pasta `cd python-week-2022`
- Você pode rodar no [https://gitpod.io](https://gitpod.io) **recomendado**
    - Para rodar no gitpod acesse no navegador `https://gitpod.io/#https://github.com/SEUNOME/python-week-2022`
    - **OBS** O plano free do github permite o uso de 40 horas do ambiente.
- Você pode rodar no [https://replit.com/](https://replit.com/) diretamente no browser
    - Para rodar no replit, crie um replit e escolha a opção `importar do github` e informe o repositório
    - **OBS** O replit.com tem limite de consumo de memória e CPU
- Ou em qualquer plataforma que permita executar Python 3.8

## Requisitos

Este template utiliza o gerenciador de pacotes **poetry**

### Se estiver rodando no Linux no seu ambiente local

`execute o comando abaixo para instalar o Poetry no Linux`
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

`Em outros ambientes pode instalar com `
```bash
pip install --user poetry
```

>  No replit.com o poetry já está disponível e no gitpod será instalado assim que o ambiente iniciar.

## Instalando o ambiente

```bash
poetry install
poetry shell
```


Executando
```bash
beerlog
# ou
python -m beerlog
```

Se apareceu `Hello from beerlog` então está tudo certo.
