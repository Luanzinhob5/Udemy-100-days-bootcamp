import requests

API_KEY = "fy9ysQu6jKZ2vcXjSiG0GmaSAkGnbULj"
API_SECRET = "AMeDrNtOYQUsrB5O"
endcode = "test.api.amadeus.com/v2"

headers = {
    "client_id":API_KEY,
    "client_secret":API_SECRET,

}

class FlightSearch():
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        # response =requests.post(url=endcode,headers=headers)
        # print(response)
        pass
    def send_iata_code(self, cities_list, sheet_list):
        for code in sheet_list:
            code["iataCode"] = "Testing"
        return sheet_list

        


