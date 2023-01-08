'''
import csv
with open("weather_data.csv") as data_file:
    weather_data = csv.reader(data_file)
    temperature = []
    for row in weather_data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)


import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avg = sum(temp_list)/len(temp_list)
print(avg)

print(data["temp"].max())

print(data["condition"])
print(data.condition)

print(data[data.temp == data.temp.max()])

'''

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_count)

red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_count)

black_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_count)

data_dict = {
    "Fur Color":["Grey","Cinnamon","Black"],
    "Count":[grey_count,red_count,black_count]
}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel Count")




