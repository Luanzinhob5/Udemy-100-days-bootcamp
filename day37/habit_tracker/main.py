import requests
from datetime import datetime

USERNAME = "lu4nb5"
TOKEN = "danwod120djas2"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": "graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()

pixel_endpoint_update = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"

pixel_endpoint_delete = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"


pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"9.0",
}

pixel_update_data = {
    "quantity":"5.0",
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

# response = requests.post(url=pixel_endpoint,json=pixel_data,headers=headers)
# print(response.text)

# response = requests.put(url=pixel_endpoint_update,json=pixel_update_data,headers=headers)
# print(response.text)

response = requests.delete(url=pixel_endpoint_update,headers=headers)
print(response.text)