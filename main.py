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
    # Consomme l'api pour les coordonnées
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
