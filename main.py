import datetime

import requests  # type: ignore
import config
import locale

# Définit la locale et la langue pour l'affichage de la date au bon format
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
country_code = "FR"

print("Météo")

# Fournit la clé d'api
api_key = config.api_key

# dictionnaire des villes
cities_dict = [
    {
        "name": "St geours de Maremne",
        "lat": "",
        "lon": "",
        "zip": "40230",
        "weather": {}
    },
    {
        "name": "Toulouse",
        "lat": "",
        "lon": "",
        "zip": "31000",
        "weather": {}
    },
    {
        "name": "Mérignac",
        "lat": "",
        "lon": "",
        "zip": "33700",
        "weather": {}
    }
]

for city in cities_dict:

    # Consomme l'api pour les coordonnées
    coordinates_results = requests.get(
        f'http://api.openweathermap.org/geo/1.0/zip?zip={city["zip"]},{country_code}&appid={api_key}'
    )

    coordinates_data = coordinates_results.json()

    city["lat"] = coordinates_data["lat"]
    city["lon"] = coordinates_data["lon"]

    # Consomme l'api pour la météo
    weather_results = requests.get(
        f'http://api.openweathermap.org/data/2.5/forecast?lat={city["lat"]}&lon={city["lon"]}&appid={api_key}&units=metric&lang=fr'
    )

    weather_data = weather_results.json()

    weather = {}

    for three_hour_forecast in weather_data["list"]:

        date = three_hour_forecast["dt_txt"].split(" ")[0]

        temp_min = three_hour_forecast["main"]["temp_min"]
        temp_max = three_hour_forecast["main"]["temp_max"]

        # Première prévision trouvée pour cette journée
        if date not in weather:
            weather[date] = {
                "temp_min": temp_min,
                "temp_max": temp_max
            }

        # Sinon on compare avec les valeurs déjà enregistrées
        else:
            if temp_min < weather[date]["temp_min"]:
                weather[date]["temp_min"] = temp_min

            if temp_max > weather[date]["temp_max"]:
                weather[date]["temp_max"] = temp_max

    city["weather"] = weather


for city in cities_dict:
    print("--------------")
    print(f'{city["name"]}')
    print("--------------")

    for date, weather in city["weather"].items():
        print(date)
        print(f'min : {weather["temp_min"]} °C')
        print(f'max : {weather["temp_max"]} °C')
        print()