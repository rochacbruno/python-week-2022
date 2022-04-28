from beerlog.core import get_beers_from_database, add_beer_to_database


def test_add_beer_to_database():
    assert add_beer_to_database("Brahma", "Pilsen", 5, 4, 7)


def test_get_beers_from_database():
    add_beer_to_database("Brahma", "Pilsen", 5, 4, 7)
    results = get_beers_from_database()
    assert len(results) > 0
