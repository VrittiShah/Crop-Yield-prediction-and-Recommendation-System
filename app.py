from flask import Flask, render_template, request
import requests
import pickle

app = Flask(__name__)

#importing the model
model = pickle.load(open('weather_data.pickle','rb'))



# Function to fetch weather data and save it to a pickle file
def get_weather_data(location):
    complete_api_link = f"{api_base_url}?q={location}&appid={user_api}"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data["cod"] == 404:
        return None
    else:
        temp = round(api_data['main']['temp'] - 273.15, 2)  # Convert temperature to Celsius
        hmdt = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']
        return {"temp": temp, "humidity": hmdt, "wind_speed": wind_speed}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    location = request.form['location']
    weather_data = get_weather_data(location)
    if weather_data:
        # Save the API response data into a pickle file
        with open('weather_data.pickle', 'wb') as f:
            pickle.dump(weather_data, f)
        return render_template('weather.html', weather_data=weather_data, location=location)
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)