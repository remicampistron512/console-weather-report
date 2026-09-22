import requests  # type: ignore
import locale
from datetime import datetime

# Définit la locale pour l'affichage de la date au bon format
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

print("Météo")
#Fournir la clé d'api
api_key = "6b7792b8d65b1ed337edd22e5afd8e96"
# définit les codes postaux
zipcode = "40230"
country_code = "FR"

#dictionnaire des villes

cities_dict = [
    {
        "name": "St geours de Maremne",
        "lat": "",
        "lon": "",
        "zip": "40230",
        "temp_min": "",
        "temp_max": ""
    },
    {
        "name": "Toulouse",
        "lat": "",
        "lon": "",
        "zip": "31000",
        "temp_min": "",
        "temp_max": ""
    },

    {
        "name": "Mérignac",
        "lat": "",
        "lon": "",
        "zip": "33700",
        "temp_min": "",
        "temp_max": ""
    }
]

for city in cities_dict:
    coordinates_results = requests.get(
        f'http://api.openweathermap.org/geo/1.0/zip?zip={city["zip"]},{country_code}&appid={api_key}')
    coordinates_data = coordinates_results.json()
    city["lat"] = coordinates_data["lat"]
    city["lon"] = coordinates_data["lon"]
    # Consomme l'api pour la météo
    weather_results = requests.get(
        f'http://api.openweathermap.org/data/2.5/forecast?lat={city["lat"]}&lon={city["lon"]}&appid={api_key}&units=metric&lang=fr')
    weather_data = weather_results.json()
    city["temp_min"] = weather_data["list"][0]["main"]["temp_min"]
    city["temp_max"] = weather_data["list"][0]["main"]["temp_max"]

for city in cities_dict:
    print("--------------")
    print(f'{city["name"]}')
    print("--------------")
    print(f'min :{city["temp_min"]} °C')
    print(f'max :{city["temp_max"]} °C')
