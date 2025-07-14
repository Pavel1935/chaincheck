import requests
from Constants import Constants

class TestGetAccessToken:

    def test_get_access_token(self):
        endpoint = "/auth/refresh-token"
        url = Constants.API_URL + endpoint

        cookies = {
            "refresh_token": "0198080a-57fe-7364-b01b-e4a372504fdd"
        }

        response = requests.post(url, cookies=cookies)

        print("RESPONSE TEXT:", response.text)

        data = response.json()

        assert data["ok"] == 1

