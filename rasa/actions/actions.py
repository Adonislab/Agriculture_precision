from typing import Dict, Text, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionMeteo(Action):
    def name(self) -> Text:
        return "action_temperature"

    def run(
        self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        # Récupérer les entités de localisation et de date
        location = tracker.get_slot("localisation")
        
        # Appeler l'API de météo avec les paramètres de localisation et de date
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=593a009514831abef5ad731958cf4e2f&units=metric&lang=fr"
        response = requests.get(url)
        data = response.json()
        
        # Extraire les informations de météo à partir de la réponse de l'API
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        precipitation = data.get("rain", {}).get("1h", 0) + data.get("snow", {}).get("1h", 0)


        # Envoyer la réponse de météo à l'utilisateur
        message = f"La température actuelle à {location} est de {temp}°C. Nous avons {weather} avec une humidité de {humidity}% et une vitesse de vent de {wind_speed} m/s. Les précipitations sont de {precipitation} mm/h."
        dispatcher.utter_message(text=message)

        return []
