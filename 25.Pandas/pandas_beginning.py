import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()

avg_temp = data["temp"].mean()
print(avg_temp)

max_temp = data["temp"].max()
print(max_temp)

print(data[data.temp == data.temp.max()])

print(data[data.day == "Monday"].temp.iloc[0] * 9/5 + 32)

data_dict = {
	"students": ["Amy", "James", "Angela"],
	"scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
