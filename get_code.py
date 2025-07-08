import time
import requests
import re

MAIL_TM_API = "https://api.mail.tm"

def read_token():
    with open("tmp_email.txt", "r") as f:
        _, token = f.read().strip().split("|")
    return token

def get_latest_email_code():
    token = read_token()
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
                code = match.group(0)
                with open("tmp_code.txt", "w") as f:
                    f.write(code)
                return code
        time.sleep(2)
    raise Exception("Код не пришёл")
