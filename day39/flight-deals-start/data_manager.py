import requests

API_URL = "https://api.sheety.co/0daf027a30850361551eab8d0ccb15b9/flightDeals/prices"
API_POST_URL = "https://api.sheety.co/0daf027a30850361551eab8d0ccb15b9/flightDeals/prices/"
# 1 - Consultar os dados da planilha com a API do sheets e salvar em um dicionario
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url=API_URL)
        # city = {text["city"]:text["lowestPrice"] for text in data["prices"]}
        
    def return_data(self):
        data = self.response.json()
        return(data)
    def upgrade_data(self,new_data):
        API_POST_URL = f"https://api.sheety.co/0daf027a30850361551eab8d0ccb15b9/flightDeals/prices/2"
        json_data = {data['city']: data['iataCode'] for data in new_data }
        response = requests.put(url=API_POST_URL,json=json_data )
        return response.raise_for_status 