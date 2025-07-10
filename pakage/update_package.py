import requests
from Constants import Constants

class TestCreatePackage:
    def test_create_package(self):
        endpoint = "/package"
        url = Constants.API_URL + endpoint

        payload = {
              "id": "199c27e9-6222-4acf-9b2b-475e4f26d05a",
              "title": "1",
              "price_usd": "111",
              "count_checks": 1,
              "ref_payout": "1",
              "status": 1
            }

        headers = {'Authorization': 'Bearer ' "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhbWwtYmFja2VuZC1nYXRld2F5Iiwic3ViIjoiMDE5MDEwYjQtYTVmZS03MmYzLTllYjUtM2E4NDg2YjY1ODY1IiwiYXVkIjpbImFtbC1iYWNrZW5kLWdhdGV3YXktdXNlcnMiXSwiZXhwIjoxNzUyMjE3NzUyLCJuYmYiOjE3NTIxMzEzNTIsImlhdCI6MTc1MjEzMTM1MiwiZmluZ2VycHJpbnQiOiJsR0xneGE2Yi9ieEhUVHVJTzlPKzdseUVrZnlmNnNQbC9EUXgxWCt6bWdvPSIsInVzZXJfcm9sZSI6M30.T6qR_3EkMX4_1uBDdV8vM7GXqfbZzcaakDRuxxkgiAU"
                            }
        response = requests.put(url, json=payload, headers=headers)
        print("RESPONSE TEXT:", response.text)

        data = response.json()

        assert data["ok"] == 1