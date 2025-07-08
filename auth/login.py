import requests
from Constants import Constants
from conftest import generate_email


class TestLogin:
    def test_login(self, generate_email):

        url = Constants.API_URL + "/auth/login"

        response = requests.post(url, json={"email": generate_email})
        print("RESPONSE TEXT:", response.text)

        data = response.json()
        assert data["ok"] == 1
