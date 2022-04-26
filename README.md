# python-week-2022

Template Para a Python Week 2022 - 25 a 29 de Abril na Linux Tips

## Instruções

Este repositório é um template de um projeto Python mínimo.  
O programa se chama `beerlog` e está organizado com pastas
e módulos, porém a maioria dos arquivos encontra-se vazio.

A partir deste template você poderá acompanhar as lives  
da Python week e programar junto com o Bruno e o Jeferson.

## Obtendo seu repositório

01. Faça login no github (cadastre-se gratuitamente caso ainda não tenha uma conta)
00. Crie um **fork** (cópia) deste repositório clicando em [fork](https://github.com/rochacbruno/python-week-2022/fork)
00. O seu repositório estará em https:// github.com / SEUNOME / python-week-2022
00. Copie a URL do seu repositório (você vai precisar depois)

## Preparando o ambiente

> **OBS**: substitua `SEUNOME` pelo seu nome de usuário do github.

- Você pode rodar localmente em seu computador desde que tenha o Python 3.8+
  - Para rodar localmente faça o clone com `git clone https://github.com/SEUNOME/python-week-2022`
  - Acesse a pasta `cd python-week-2022`
- Você pode rodar no [https://gitpod.io](https://gitpod.io) **recomendado**
  - Para rodar no gitpod acesse no navegador `https://gitpod.io/#https://github.com/SEUNOME/python-week-2022`
  - **OBS**: O plano free do gitpod permite o uso de 40 horas do ambiente.
- Você pode rodar no [https://replit.com/](https://replit.com/) diretamente no browser
  - Para rodar no replit, crie um replit e escolha a opção `importar do github` e informe o repositório
  - **OBS**: O replit.com tem limite de consumo de memória e CPU
- Ou em qualquer plataforma que permita executar Python 3.8

## Requisitos

Este template utiliza o gerenciador de pacotes **poetry**

### Se estiver rodando no Linux no seu ambiente local

`execute o comando abaixo para instalar o Poetry no Linux`

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

`Em outros ambientes pode instalar com`

```bash
pip install --user poetry
```

> No replit.com o poetry já está disponível e no gitpod será instalado assim que o ambiente iniciar.

## Instalando o ambiente

O comando a seguir instala as dependências do projeto.

```bash
poetry install
```

O comando a seguir ativa o ambiente virtual do poetry

```bash
poetry shell
```

> **IMPORTANTE** o ambiente precisa estar ativado para o programa executar.  
> No terminal aparecerá algo como  
> `(beerlog-DlEBh_72-py3.8) gitpod /workspace/python-week-2022 (main) $`

Executando o programa

```bash
beerlog
# ou
python -m beerlog
```

Se apareceu `Hello from beerlog` então está tudo certo.


## Está com problemas com instalação ou autocomplete no gitpod?

### Poetry

Para o programa rodar o ambiente poetry precisa estar ativado

```
pip install poetry
poetry install
poetry shell
```

Ou execute `source start_poetry` que é um script que automatiza os comandos acima.

### Autocomplete não funciona?

Após ativar o poetry digite no terminal

```
which python 
```
A saida será algo como

```
/home/gitpod/.cache/pypoetry/virtualenvs/beerlog-DlEBh_72-py3.8/bin/python
```

Copie este path ^

Agora digite `F1` no gitpod ou `Ctrl + Shift + P` no Vscode local e selectione a opção `Python: Select Interpreter`
Cole o path `/home/gitpod/.cache/pypoetry/virtualenvs/beerlog-DlEBh_72-py3.8/bin/python` e digite enter.

> **OBS**: Pode ser que o caminho seja outro, o importante é terminar com `/bin/python`