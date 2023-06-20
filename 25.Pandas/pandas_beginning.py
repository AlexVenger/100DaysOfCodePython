import pandas

# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
#
# avg_temp = data["temp"].mean()
# print(avg_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data[data.temp == data.temp.max()])
#
# print(data[data.day == "Monday"].temp.iloc[0] * 9/5 + 32)
#
# data_dict = {
# 	"students": ["Amy", "James", "Angela"],
# 	"scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = ["Gray", "Cinnamon", "Black"]
squirrel_count = []
for color in fur_color:
    squirrel_count.append(len(squirrel_data[squirrel_data["Primary Fur Color"] == color]))
new_data = pandas.DataFrame({"Fur Color": fur_color, "Count": squirrel_count})
new_data.to_csv("new_data.csv")
