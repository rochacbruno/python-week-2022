# Links

- https://github.com/rochacbruno/python-week-2022
- https://replit.com
- https://gitpod.io/#

# Script

Boas vindas [...]

## Preparando o ambiente

Preparamos um repositorio de template

https://github.com/rochacbruno/python-week-2022


Explicar as pastas do repositório.


## Intro a Python

Python é uma linguagem dinâmica criada no inicio dos anos 90
que está completando 32 anos e continua evoluindo muito.

As principais caracteristicas da linguagem são o seu foco em
legibilidade sendo uma das linguagens mais fáceis de aprender
e o fato de ter tipagam forte, porém dinâmica.

Python é uma linguagem muito utilizada para backend em ambiente
web, para automação de processos, computação gráfica servindo de
linguagem de script e integração e também na area de dados.

Os programas Python são interpretados e para abrir o interpretador
basta digitar `python` no terminal.

> Essa ferramenta é chamada de REPL e portanto o print é implicito.

```bash
>>> 1 + 1
2
>>> "python".upper()
PYTHON
>>> sum([1,2,3,4])
10
```

Também podemos colocar esses comandos organizados em um `script` com a extensão
`.py` e executar

> neste caso precisamos do `print` explicito.

`script.py`
```py
print(1 + 1)
print("python".upper())
print(sum([1,2,3,4]))
```
```bash
$ python script.py
2
PYTHON
10
```

Os tipos de dados em Python estão divididos entre primitivos e compostos,
sendo os principais:

- `int`
- `float`
- `str`
- `bool`
- `None`

e

- `tuple`
- `list`
- `set`
- `dict`

E uma série de tipos especiais como `type` e `function`.


Exemplo de um programa em Python usando os principais componentes da linguagem.

`script.py`
```py
event = "Python Week"
topics = ["\N{snake} Python", "\N{whale} Containers", "\N{penguin} Linux"]

days = {
    1: "Introdução a Python",
    2: "Python para web",
    3: "Qualidade de código, testes e CI",
    4: "Análise de dados",
    5: "Perguntas"
}

print(f"Boas vindas a {event} - um evento de {len(days)} dias")
for topic in topics:
    print(f"{topic.upper()}")

for day, title in days.items():
    print(f"{day} -> {title}")
    if day == 1:
        print("\t é Hoje!!!")
```

No exemplo acima perceba que os blocos lógicos do programa são separados por
identação (recuo) formado por 4 espaços.

## Projeto

Ao digitar beerlog no ambiente instalado a partir do repositório

```bash
$ beerlog
Hello from beerlog
```

O  projeto que vamos construir agora se chama `beerlog` e será um programa
de terminal para o Jeferson guardar o histórico de cervejas que ele toma
aqui durante as gravações da LinuxTips.


Adicionar cerveja no banco de dados
```bash
$beerlog add "Lagunitas" IPA --flavor=10 --image=10 --cost=8
```

> O programa irá calcular a média da avaliação e salvar no campo `rate`

Visualizar as cervejas

```text
$ beerlog list --style=IPA
                              Beerlog IPA                               
┏━━━━┳━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━━━━━━━┓
┃ id ┃ name        ┃ style ┃ flavor ┃ image ┃ cost ┃ rate ┃ date       ┃
┡━━━━╇━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━╇━━━━━━╇━━━━━━━━━━━━┩
│ 2  │ Lagunitas   │ IPA   │ 10     │ 10    │ 5    │ 8    │ 2022-04-22 │
│ 5  │ New Ocen    │ IPA   │ 10     │ 10    │ 5    │ 8    │ 2022-04-22 │
└────┴─────────────┴───────┴────────┴───────┴──────┴──────┴────────────┘
```

### Parte 1 - Modelagem de dados:

A maior parte dos programas nasce a partir da modelagem de dados.

> **importante** Abra a aba de comandos do VSCode `F1 no gitpod, ctrl+P em outros` e selecione
> Python select interpreter, e escolha a opção do poetry.

#### Dataclasses 101

No arquivo `beerlog/models.py` vamos começár usando `dataclass` que é a forma mais
fácil de definir objetos para armazenar dados em Python.

```py
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Beer:
    id: int
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = field(default_factory=datetime.now)


beer = Beer(1, "Lagunitas", "IPA", 9, 10, 8)
```

Para executar em modo interativo no terminal.
```bash
ipython -i beerlog/models.py
```
```
In [1] beer.name
Lagunitas
```

#### ORM

Os dados precisam ficar persistidos e para isso usaremos um banco de dados SQL.

Nós vamos usar uma bilbioteca chamada **SQLModel** para fazer o mapeamento de
classes em Python para tabelas em banco de dados SQL.

No arquivo `beerlog/models.py` vamos substituir dataclass por SQLModel.

```py
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)


beer = Beer(name="Lagunitas", style="IPA", flavor=9, image=10, cost=8)
```

#### SQLAlchemy

Executando em modo interativo agora podemos ver os comandos SQL que nossa classe
é capaz de gerar.

```bash
ipython -i beerlog/models.py
```
```py
In [1]: from sqlmodel import select
In [2]: print(select(Beer))

SELECT beer.id, beer.name, beer.style, beer.flavor, beer.image, beer.cost, beer.rate, beer.date
FROM beer

In [3]: print(select(Beer).where(Beer.style == "IPA"))

SELECT beer.id, beer.name, beer.style, beer.flavor, beer.image, beer.cost, beer.rate, beer.date
FROM beer
WHERE beer.style = :style_1
```

#### Pydantic

O SQLModel utiliza uma biblioteca chamada Pydantic para fazer validação
e serialização de dados.

Vamos aplicar algumas regras:

- As notas de `flavor`, `image`, `cost` só podem ser numeros de 1 a 10.
- O campo `rate` que é a nota média da cerveja será calculado com base
  nesses valores.


```py
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from pydantic import validator  # NEW
from statistics import mean  # NEW


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    # NEW
    @validator("image", "flavor", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    # NEW
    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)
```

### Parte 2 - Conectando ao banco de dados

O Python já tem embutido o SQLite então pela simplicidade vamos utiliza-lo.

Precisaremos

- Definir uma conexão com o banco de dados
- Criar a tabela a partir do models usando a DDL do SQL
- Definir uma `session` um objeto que permita executar comandos SQL através
  do Python.

`beerlog/database.py`

```py
from sqlmodel import create_engine

from beerlog import models
from beerlog.config import settings

engine = create_engine("sqlite:///beerlog.db", echo=False)
models.SQLModel.metadata.create_all(engine)
```

> Aqui poderiamos usar Mysql ou Postgresql apenas trocando a string de conexão.

Ao invés de passar a string de conexão diretamente, podemos utilizar
uma variavél de configuração:

`beerlog/settings.toml`
```toml
[database]
url = "sqlite:///beerlog.db"
```

E então alterar o `database.py`

```py
from sqlmodel import create_engine

from beerlog import models
from beerlog.config import settings  # NEW

engine = create_engine(settings.database.url, echo=False)  # NEW
models.SQLModel.metadata.create_all(engine)
```

Ao executar `python beerlog/database.py` teremos o banco de dados `beerlog.db`
criado no caminho especificado (raiz do repositório).

O SQLModel irá gerar as instruçòes `DDL` do SQL para criar as tabelas.

A vantagem de usar um gerenciador de configurações como o Dynaconf é a
possibilidade de sobrescrever os settings via variaveis de ambiente.

```bash
export BEERLOG_database__url = "sqlite:///testing.db"
python beerlog/database.py
...
unset BEERLOG_database__url
```

> **NOTA** em um programa em produção este database geralmente ficaria em `/etc/beerlog` ou `/var/lib/beerlog` 

#### DML e DQL (a.k.a CRUD)

Agora podemos usar a extensao **SQLite** ou `sqlite3 beerlog.db` para se comunicar
com o banco de dados.

```sql
INSERT INTO beer (name, style, flavor, image, cost, rate, date)
VALUES ("Heineken", "Lager", 5, 5, 5, 5, "2022-04-22 13:25:31.021979");

SELECT * FROM beer;

UPDATE beer set style="IPA";

DELETE from beer;
```

> OBS: `.quit` para sair do terminal `sqlite3`


#### Fazendo operações CRUD através do Python

O primeiro passo é obter uma `session` e o SQLmodel oferece isso através do
objeto `Session`.

`beerlog/database.py`
```py
from sqlmodel import create_engine, Session  # NEW

from beerlog import models
from beerlog.config import settings

engine = create_engine(settings.database.url, echo=False)
models.SQLModel.metadata.create_all(engine)


# NEW
def get_session():
    return Session(engine)
```

E agora para interagir com o banco de dados precisamos de 3 objetos:

```bash
$ ipython
```
```py
from beerlog.database import get_session
from beerlog.models import Beer
from sqlmodel import select

session = get_session()
```

Adicionando novas cervejas

```py
beer = Beer(name="Lagunitas", style="IPA", flavor=10, image=10, cost=5)
session.add(beer)
session.commit()
```

Selecionando cervejas

```py
for beer in session.exec(select(Beer).where(Beer.style == "IPA")):
    print(beer.name, beer.style, beer.rate)
```

> **NOTA** se quiser esconder os warnigns do SQlAlchemy

No topo de `beerlog/database.py` coloque as linhas:
```py
import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar
warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
```


### Parte 3 - Criando a interface de linha de comando

Definição dos comandos:

Nosso programa tem 2 comandos `add` e `list`

No arquivo `beerlog/cli.py` vamos apagar o código atual e escrever:

```py
import typer

main = typer.Typer(help="Beer Management Application")


@main.command()
def add(name: str, style: str):
    """Adds a new beer to the database"""


@main.command("list")
def list_beers():
    """Lists beers from the database"""
```

Ao executar `beerlog --help` no terminal

```bash
$ beerlog --help
Usage: beerlog [OPTIONS] COMMAND [ARGS]...

  Beer Management Application

Options:
  --help                          Show this message and exit.

Commands:
  add   Adds a new beer to the database
  list  Lists beers from the database
```

E `beerlog add --help`

```bash
$ beerlog add --help
Usage: beerlog add [OPTIONS] NAME STYLE

  Adds a new beer to the database

Arguments:
  NAME   [required]
  STYLE  [required]

Options:
  --help  Show this message and exit.
```

Vamos adicionar o restante das opções e a chamada para o código que irá
se comunicar com o banco de dados.

```py
import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database


main = typer.Typer(help="Beer Management Application")


@main.command()
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to the database"""
    if add_beer_to_database(name, style, flavor, image, cost):
       print("\N{beer mug} Beer added!!!")
    else:
        print("\N{no entry} - Cannot add beer.")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers from the database"""
    beers = get_beers_from_database(style)
    print(beers)
```

Se você tentar rodar agora vai obter um erro dizendo que as funções
`add_beer` e `get_beers` não existem.

```bash
ImportError: cannot import name 'add_beer_to_database' from 'beerlog.core'
```

Agora precisamos abrir o arquivo `beerlog/core.py` e implementar as funções,
e o motivo de colocarmos essas funções no arquivo `core` ao invés de chamar
o banco de dados diretamente no `cli` é o fato de `cli`ser um `front-end`
e front-ends devem ser desacoplados da lógica principal do programa.


```py
from typing import Optional, List
from sqlmodel import select
from beerlog.database import get_session
from beerlog.models import Beer


def add_beer_to_database(
    name: str,
    style: str,
    flavor: int,
    image: int,
    cost: int,
) -> bool:
    with get_session() as session:
        beer = Beer(
            name=name,
            style=style,
            flavor=flavor,
            image=image,
            cost=cost,
        )
        session.add(beer)
        session.commit()

    return True


def get_beers_from_database(style: Optional[str] = None) -> List[Beer]:
    with get_session() as session:
        sql = select(Beer)
        if style:
            sql = sql.where(Beer.style == style)
        return list(session.exec(sql))
```

A função `add_beer_to_database` pode ficar mais simples:

```py
def add_beer_to_database(
    name: str,
    style: str,
    flavor: int,
    image: int,
    cost: int,
) -> bool:
    with get_session() as session:
        beer = Beer(**locals())
        session.add(beer)
        session.commit()

    return True
```

### Parte 4 - Deixando bonito

Ao executar `beerlog list` a saida do comando está um pouco **feia** vamos
adicionar um pouco de estilo.

e vamos transformar isso

```py
$ beerlog list
[Beer(image=10, name='aaa', flavor=10, rate=10, style='bbb', id=1, cost=10, date=datetime.datetime(2022, 4, 22, 13, 25, 31, 21979)), Beer(image=10, name='Lagunitas', flavor=10, rate=8, style='IPA', id=2, cost=5, date=datetime.datetime(2022, 4, 22, 13, 25, 31, 21979)), Beer(image=5, name='Heineken', flavor=5, rate=5, style='Lager', id=3, cost=5, date=datetime.datetime(2022, 4, 22, 13, 25, 31, 21979)), Beer(image=5, name='Heineken', flavor=5, rate=5, style='Lager', id=4, cost=5, date=datetime.datetime(2022, 4, 22, 13, 25, 31, 21979)), Beer(image=10, name='Lagunitas 2', flavor=10, rate=8, style='IPA', id=5, cost=5, date=datetime.datetime(2022, 4, 22, 13, 50, 57, 766305)), Beer(image=10, name='Heineken', flavor=10, rate=10, style='Lager', id=6, cost=10, date=datetime.datetime(2022, 4, 22, 15, 12, 52, 242539)), Beer(image=10, name='Heineken', flavor=10, rate=10, style='Lager', id=7, cost=10, date=datetime.datetime(2022, 4, 22, 15, 15, 40, 571529)
```

Usando:

```py
import typer
from typing import Optional
from rich.console import Console  # NEW
from rich.table import Table  # NEW
from rich import print  # NEW

from beerlog.core import add_beer_to_database, get_beers_from_database


main = typer.Typer(help="Beer Management Application")
console = Console()


@main.command()
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to the database"""
    if add_beer_to_database(name, style, flavor, image, cost):
       print(":beer_mug: Beer added!!!")  # NEW
    else:
        print(":no_entry: - Cannot add beer.")  # NEW


# NEW
@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers from the database"""
    beers = get_beers_from_database(style)
    table = Table(title="Beerlog Database" if not style else f"Beerlog {style}")
    headers = ["id", "name", "style", "flavor", "image", "cost", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
```
Nisso

```bash
$ beerlog list --style=IPA
                              Beerlog IPA
┏━━━━┳━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━━━━━━━┓
┃ id ┃ name        ┃ style ┃ flavor ┃ image ┃ cost ┃ rate ┃ date       ┃
┡━━━━╇━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━╇━━━━━━╇━━━━━━━━━━━━┩
│ 2  │ Lagunitas   │ IPA   │ 10     │ 10    │ 5    │ 8    │ 2022-04-22 │
│ 5  │ Lagunitas 2 │ IPA   │ 10     │ 10    │ 5    │ 8    │ 2022-04-22 │
└────┴─────────────┴───────┴────────┴───────┴──────┴──────┴────────────┘
```


Agora no dia 2 vamos criar uma API para o `beerlog` até amanhã! 