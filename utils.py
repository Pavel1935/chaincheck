import requests
import time
import re

MAIL_TM_API = "https://api.mail.tm"

def create_temp_email():
    domain_resp = requests.get(f"{MAIL_TM_API}/domains")
    domain = domain_resp.json()["hydra:member"][0]["domain"]
    address = f"test{int(time.time())}@{domain}"
    password = "testpassword"

    requests.post(f"{MAIL_TM_API}/accounts", json={
        "address": address,
        "password": password
    })

    token_resp = requests.post(f"{MAIL_TM_API}/token", json={
        "address": address,
        "password": password
    })
    token = token_resp.json()["token"]

    return address, token


def get_latest_email_code(token):
    headers = {"Authorization": f"Bearer {token}"}

    for _ in range(30):
        resp = requests.get(f"{MAIL_TM_API}/messages", headers=headers)
        messages = resp.json()["hydra:member"]
        if messages:
            msg_id = messages[0]["id"]
            msg_resp = requests.get(f"{MAIL_TM_API}/messages/{msg_id}", headers=headers)
            body = msg_resp.json()["text"]
            match = re.search(r"\b\d{6}\b", body)
            if match:
                return match.group(0)
        time.sleep(2)

    raise Exception("Код не пришёл")