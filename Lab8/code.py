from urllib import response
import requests, json
api_key = "e749f314a77d14fb5c5eae40a58eec64"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="
city_name = input("Nhập tên thành phố của bạn: ")
complete_url = base_url+city_name+"&appid="+api_key
response = requests.get(complete_url)
data=response.json()
print(data)
print("Nhiệt độ thực tế: ", round(data["main"]["temp"]-273, 2),"°C")
print("Nhiệt độ hiện tại: ", round(data["main"]["feels_like"]-273, 2),"°C")
print("Nhiệt độ tối đa: ", round(data["main"]["temp_max"]-273, 2),"°C")
print("Nhiệt độ tối thiểu: ", round(data["main"]["temp_min"]-273, 2),"°C")