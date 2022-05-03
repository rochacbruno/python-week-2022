import pytest
from unittest.mock import patch
from sqlmodel import create_engine
from beerlog import models


@pytest.fixture(autouse=True, scope="function")
def each_test_uses_separate_database(request):
    tmpdir = request.getfixturevalue("tmpdir")
    test_db = tmpdir.join("beerlog.test.db")
    engine = create_engine(f"sqlite:///{test_db}")
    models.SQLModel.metadata.create_all(bind=engine)
    with patch("beerlog.database.engine", engine):
        yield
