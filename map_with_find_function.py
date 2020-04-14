import folium
import sys
import requests
import os
import random



toponym_to_find = 'Москва'

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    # обработка ошибочной ситуации
    pass

# Преобразуем ответ в json-объект
json_response = response.json()

# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
# Координаты центра топонима:
s1 = toponym["Point"]["pos"]  # Координаты точки
# Долгота и широта:
toponym_longitude, toponym_lattitude = s1.split(" ")

address_ll = toponym_longitude + "," + toponym_lattitude

search_params = {
    "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
    "text": "KFC",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

search_api_server = "https://search-maps.yandex.ru/v1/"
response = requests.get(search_api_server, params=search_params)
if not response:
    pass
# Преобразуем ответ в json-объект
json_response = response.json()


# Координаты центра топонима:

# Долгота и широта:

# Получаем первую найденную организацию.

organization = json_response["features"][0]
# Название организации.
org_name = organization["properties"]["CompanyMetaData"]["name"]
# Адрес организации.
org_address = organization["properties"]["CompanyMetaData"]["address"]
# Время работы
org_time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]

# Получаем координаты ответа.
k = []
coords1 = []
s2 = organization["geometry"]["coordinates"]
for i in json_response["features"]:
    k.append(i["geometry"]["coordinates"])
for i in k:
    x = str(i[0])
    x += ','
    x += str(i[1])
    coords1.append(x)

map = folium.Map(location=[toponym_lattitude, toponym_longitude], zoom_start = 11)
s1 = s1.split()
spis = []
for i in range(len(coords1)):
    check = coords1[i]
    check = check.split(',')
    s1[0] = float(s1[0])
    s1[1] = float(s1[1])
    x1 = float(s1[0])
    x2 = float(check[0])
    y1 = float(s1[1])
    y2 = float(check[1])
    spis.append([x2, y2])

for i in json_response["features"]:
    k.append(i["geometry"]["coordinates"])
    h = i["properties"]["CompanyMetaData"].get("Hours", None)
    if h:
        available = h["Availabilities"][0]
        if available.get("Everyday", False) and available.get("TwentyFourHours", False):
            coloor = 'green'
        else:
            coloor = 'red'
    else:  # Данных о времени работы нет.
        coloor = 'grey'

for lat, lon in spis:
    folium.Marker(location=[lon, lat], icon=folium.Icon(color = coloor)).add_to(map)

map.save("map1.html")