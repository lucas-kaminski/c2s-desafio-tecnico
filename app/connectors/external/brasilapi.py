import requests


class BrasilAPI:
    def __init__(self):
        self.base_url = "https://brasilapi.com.br/api"

    def _get(self, url: str):
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        json_data = response.json()
        return json_data

    def get_all_car_brands(self):
        url = f"{self.base_url}/fipe/marcas/v1/carros"
        response = self._get(url)
        return response

    def get_all_cars_by_brand(self, brand_id: str):
        url = f"{self.base_url}/fipe/veiculos/v1/carros/{brand_id}"
        response = self._get(url)
        return response
