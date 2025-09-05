from config.config import BASE_URL, API_KEY, HEADERS, TIMEOUT
import requests
import pytest
import src
from src.utils import load_json
from src.client import APIClient
test_data = load_json("C:/Projects/api_testing/tests/test_data.json")



api = APIClient(BASE_URL)
@pytest.mark.parametrize("city", test_data["valid_cities"])
def test_weather_valid_city(city):


    resp = api.get(
        "/weather",
        params={"q": city["name"], "appid": API_KEY},
        headers=HEADERS,
        timeout=TIMEOUT,
    )
    src.utils.assert_status_code(resp, 200)

    data = resp.json()
    assert data["name"] == city["name"]


    for field in test_data["expected_fields"]:
        assert field in data


@pytest.mark.parametrize("city", test_data["invalid_cities"])
def test_weather_invalid_city(city):
    resp = api.get(
        "/weather",
        params={"q": city["name"], "appid": API_KEY},
        headers=HEADERS,
        timeout=TIMEOUT,
    )
    src.utils.assert_status_code(resp, city["expected_status"])