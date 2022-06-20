# file = open("weather_data.csv", "r")
# data = file.read()
# new_data = data.split()
# new_list = []
# for i in new_data:
#     new_list.append(i.split())
# print(new_list)

# import csv
# file = open("weather_data.csv", "r")
# data = csv.reader(file)
# temperature = []
# # for row in data:
# #     print(row)
# for i in data:
#     if i[1].isdigit() is True:
#         temperature.append(int(i[1]))
# print(temperature)

import pandas
# from statistics import mean
# data = pandas.read_csv("weather_data.csv")
# # max_temp = data[data["temp"]  == data["temp"].max()]
# # print(max_temp)
# temp = data[data.day == "Monday"]
# c_temp = int(temp.temp)
# f_temp = (c_temp * 1.8) + 32
# print(f_temp)


# print(data[data["day"] == "Monday"])
#count each color of squirrl and create new dataframe
# data = pandas.read_csv("CentralPark.csv")
# new_data = data["Primary Fur Color"] == "Gray"
# print(data.count())

# data = pandas.read_csv("weather_data.csv")
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# print(pandas.DataFrame(data_dict))

data = pandas.read_csv("CentralPark.csv")
color = data["Primary Fur Color"]

gray = 0
red = 0
black = 0

for i in color:
    if i == "Gray":
        gray += 1
    if i == "Black":
        black += 1
    if i == "Cinnamon":
        red += 1

dict = {}
dict["Fur Color"] = ["grey", "red", "black"]
dict["Count"] = [gray, black, red]

df = pandas.DataFrame(dict)
df.to_csv("squirrel_count.csv")


