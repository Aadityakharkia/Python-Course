# Habit Tracker

# Website -- https://pixe.la/
# Api Documentation

import requests
from datetime import datetime


token = "Your Token"
username = "Your Username"

headers = {
    "X-USER-TOKEN":token
}

pixela_endpoint = "https://pixe.la/v1/users"


#---------------------- Setting up the environment & Creating a ID with a token and Username ---------------------

parameters = {
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#response = requests.post(url=pixela_endpoint,json=parameters)
#print(response.text)

#---------------------- Creating a graph called cycling Graph with different parameters ---------------------------

graph_Endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_parameters = {
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"shibafu"
}

#response = requests.post(url=graph_Endpoint,json=graph_parameters,headers=headers)
#print(response.text)

#---------------------- Inserting values in the graph using different parameters ----------------------------------

today = datetime.now()

graph_filling = f"{graph_Endpoint}/graph1"

graph_filling_parameters = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"3"
}

response = requests.post(url=graph_filling,json=graph_filling_parameters,headers=headers)
print(response.text)

#---------------------- Future Works and Improvements ---------------------------------------------------------------

# Creating a automated system and implementing GUI.
# Including different graphs and other datas