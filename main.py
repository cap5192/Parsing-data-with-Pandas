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

data = pandas.read_csv("CentralPark.csv")
new_data = data["Primary Fur Color"] == "Gray"
print(data.count())