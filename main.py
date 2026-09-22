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


# Consomme l'api pour les coordonnées
coordinates_results = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{country_code}&appid={api_key}')
coordinates_data = coordinates_results.json()
print (coordinates_data)

#Récuperer la latitude et la longitude

latitude = coordinates_data["lat"]
longitude = coordinates_data["lon"]
# Consomme l'api pour la météo
weather_results = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}')
weather_data = weather_results.json()

print(weather_data)




# Définir les unités


#Récupérer la température minimale pour les 5 jours a venir à Mérignac, Saint-Geours-de-Maremne et Toulouse

#Récupérer la température maximale pour les 5 jours a venir à Mérignac, Saint-Geours-de-Maremne et Toulouse



