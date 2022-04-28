from fastapi.testclient import TestClient

from beerlog.api import api

client = TestClient(api)


def test_create_beer_via_api():
    response = client.post(
        "/beers/",
        json={
            "name": "Lagunitas",
            "style": "IPA",
            "flavor": 8,
            "image": 8,
            "cost": 8,
        },
    )
    assert response.status_code == 200
    result = response.json()
    assert result["name"] == "Lagunitas"
    assert result["id"] == 1
