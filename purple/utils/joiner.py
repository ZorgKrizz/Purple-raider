from utils.sync import get_cookies, get_headers
import requests

class Joiner:
    def __init__(self):
        with open("tokens.txt", "r") as file:
            self.tokens = file.readlines()

    def join(self, link, token):
        url = f"https://discord.com/api/v9/invites/{link}"
        session = requests.Session()
        session.cookies.update(get_cookies(token))

        response = session.post(url, headers=get_headers(token), json={"session_id": "594d8df69250df37d644ee23a0c3d564"})

        print(response.status_code)

    
