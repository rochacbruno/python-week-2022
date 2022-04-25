<<<<<<< HEAD
from sqlmodel import create_engine
from beerlog.config import settings
from beerlog import models

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)
=======
import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


from sqlmodel import create_engine, Session

from beerlog import models
from beerlog.config import settings

engine = create_engine(settings.database.url, echo=False)
models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
>>>>>>> 9fa577c44e80f0c41d317674351b6fbad26dbd2c
