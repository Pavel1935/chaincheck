import requests
from Constants import Constants

class TestGetAccessToken:

    def test_get_access_token(self):
        endpoint = "/Auth/refresh-token"
        url = Constants.API_URL + endpoint

        cookies = {
            "refresh_token": Constants.REFRESH_TOKEN
        }

        response = requests.post(url, cookies=cookies)

        print("RESPONSE TEXT:", response.text)

        data = response.json()

        assert data["ok"] == 1

