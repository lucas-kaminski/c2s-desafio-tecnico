import requests

from app.config import SERVER_URL


class MCPClient:
    def __init__(self):
        self.base_url = SERVER_URL

    def call_function(self, function_name: str, params: dict):
        url = f"{self.base_url}/{function_name}"
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            raise Exception(f"Erro na chamada {function_name}: {response.text}")

        return response.json()
