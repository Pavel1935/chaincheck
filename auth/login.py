import requests
from Constants import Constants
from conftest import generate_email


class TestLogin:
    def test_login(self):

        url = Constants.API_URL + "/Auth/login"

        response = requests.post(url, json={"email": Constants.EMAIL})
        print("RESPONSE TEXT:", response.text)

        data = response.json()
        assert data["ok"] == 1
