import datetime as dt
import requests
import pickle

user_api = "c4aecb96ff9cc061757449c3891e33a4"
location = input("Enter the city name:")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data["cod"] == "404":
    print("Invalid city")
else:
    temp = ((api_data['main']['temp']) - 273.15)
    hmdt = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']

    print("Current Temperature is {:.2f} deg C:".format(temp))
    print("Current Humidity:", hmdt)
    print("Wind Speed:", wind_speed)

    # Save the API response data into a pickle file
    with open('weather_data.pickle', 'wb') as f:
        pickle.dump(api_data, f)

