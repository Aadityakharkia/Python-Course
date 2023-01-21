import requests
from datetime import datetime

token = "asdfghjjklkjhgfdsa"
username = "aadityakharkia"

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token":"asdfghjjklkjhgfdsa",
    "username":"aadityakharkia",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#response = requests.post(url=pixela_endpoint,json=parameters)
#print(response.text)

graph_Endpoint = f"{pixela_endpoint}/{username}/graphs"

headers = {
    "X-USER-TOKEN":token
}

graph_parameters = {
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"shibafu"
}

#response = requests.post(url=graph_Endpoint,json=graph_parameters,headers=headers)
#print(response.text)

today = datetime.now()

graph_filling = f"{graph_Endpoint}/graph1"

graph_filling_parameters = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"3"
}

response = requests.post(url=graph_filling,json=graph_filling_parameters,headers=headers)
print(response.text)