import pytest
import requests
from Constants import Constants
import time
import re
import random
import string

from create_email import create_temp_email


@pytest.fixture
def access_token():
    endpoint = "/auth/refresh-token"
    url = Constants.API_URL + endpoint

    cookies = {
        "refresh_token": Constants.REFRESH_TOKEN
    }

    response = requests.post(url, cookies=cookies)
    token = response.json()

    assert token["ok"] == 1
    assert "access_token" in token
    print("ACCESS TOKEN:", token["access_token"])

    return token["access_token"]

аптавтвпртвптвтп



def generate_email():
    login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = "1secmail.com"
    return login, domain, f"{login}@{domain}"


def fetch_verification_code(login, domain):
    base_url = "https://www.1secmail.com/api/v1/"

    for _ in range(10):
        resp = requests.get(base_url, params={
            "action": "getMessages",
            "login": login,
            "domain": domain
        })

        messages = resp.json()
        if messages:
            msg_id = messages[0]["id"]
            msg = requests.get(base_url, params={
                "action": "readMessage",
                "login": login,
                "domain": domain,
                "id": msg_id
            }).json()

            body = msg.get("textBody", "")
            match = re.search(r"\b\d{6}\b", body)
            if match:
                return match.group(0)

        time.sleep(3)

    return None


@pytest.fixture(scope="session")
def verification_code():
    login, domain, email = generate_email()
    print(f"📧 Generated temp email: {email}")

    # 👉 отправь на него письмо в тесте логина (отдельно)

    code = fetch_verification_code(login, domain)
    print(f"📩 Received verification code: {code}")

    return email, code
