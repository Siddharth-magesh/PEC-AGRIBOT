import json
import requests

def load_temp(loc):
    with open('location.json', 'r') as file:
        data = json.load(file)
        for item in data:
            if item['location'].lower() == loc.lower():
                lati = item['latnlon']['lat']
                long = item['latnlon']['lon']
                response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lati}&lon={long}&appid=3a828979b8653572ed653e4535eb8747")
                x = response.json()
                temp = x['main']['temp']
                humidity = x['main']['humidity']
                return ("the current temperature is : ",int(temp-273)," and the humidity is ",humidity)

