# with open("Day_25\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Day_25\weather_data.csv") as data_file:
#     data  = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("Day_25/weather_data.csv")
# print(data["temp"])
# print(data)

# data_dict = data.to_dict()
# print(data_dict["day"])

# temp_list = data["temp"].tolist()
# avg = 0
# for temp in temp_list:
#     avg += int(temp)
# avg = avg / len(temp_list)
# print(avg)


# print(data["temp"].mean())


# print(data[data.day == "Monday"])


# Create a dataframe from scratch

data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data=data_dict)
data.to_csv("new_data.csv")