from beerlog.core import get_beers_from_database, add_beer_to_database


def test_add_beer_to_database():
    # ARRANGE
    assert add_beer_to_database("Blue Moon", "Witbier", 10, 3, 6)
    # ACT
    results = get_beers_from_database()
    # ASSERT
    assert len(results) > 0

