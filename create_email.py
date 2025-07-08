import requests
import time

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

    # сохраняем во временный файл
    with open("tmp_email.txt", "w") as f:
        f.write(f"{address}|{token}")

    return address, token