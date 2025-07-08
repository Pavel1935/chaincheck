import pytest
import requests
from Constants import Constants
from conftest import generate_email, verification_code

class TestVerifyEmail:
    def test_verify_email(self, generate_email, verification_code):
        if not verification_code:
            pytest.skip("Не удалось получить код из почты")

        endpoint = "/auth/verify-email"
        url = Constants.API_URL + endpoint

        body = {
            "email": generate_email,
            "code": verification_code
        }

        response = requests.post(url, json=body)
        print("RESPONSE TEXT:", response.text)

        data = response.json()
        assert data["ok"] == 1