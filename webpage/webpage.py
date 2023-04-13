from flask import Flask, redirect, url_for, render_template
import sys
sys.path.insert(0, r'')
from dags.updateInfo import updateWeather
from dags.weather10days import day2, day3, day4, day5, day6, day7, day8, day9
from flask import url_for

date_, today_celcius, today_weather, wind_kmh, humidity, dewpoint_celcius, pressure_barometric, uv_index, visibilty, moon_phase = updateWeather()
print(str(today_weather))
print(str(day2[3]))
print(str(day3[3]))
print(str(day4[3]))
print(str(day5[3]))
print(str(day6[3]))
print(str(day7[3]))
print(str(day8[3]))
print(str(day9[3]))

def switch(argument):
    switcher = {
        'Cloudy': 'cloudy.png',
        'Mostly,Cloudy': 'cloudy.png',
        'Partly,Cloudy': 'partlycloudy.png',
        'Rain': 'rain.png',
        'Rain,Rain': 'rain.png',
        'Scattered,Showers': 'rain.png',
        'Snowing' : 'snowing.png',
        'Storm' : 'storm.png',
        'Mostly,Sunny' : 'sunny.png',  
        'Sunny,Sunny' : 'sunny.png',   
    }
    return switcher.get(argument)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    
    image_weather_today = switch(today_weather)
    image_weather_day2 = switch(day2[3])
    image_weather_day3 = switch(day3[3])
    image_weather_day4 = switch(day4[3])
    image_weather_day5 = switch(day5[3])
    image_weather_day6 = switch(day6[3])
    image_weather_day7 = switch(day7[3])
    image_weather_day8 = switch(day8[3])
    image_weather_day9 = switch(day9[3])
    print(day2[3], day3[3], day4[3], day5[3], day6[3], day7[3], day8[3], day9[3])

    return render_template('index.html', image_weather_today = image_weather_today, image_weather_day2 = image_weather_day2,
                           image_weather_day3 = image_weather_day3, image_weather_day4= image_weather_day4, 
                           image_weather_day5 = image_weather_day5, image_weather_day6 = image_weather_day6,
                           image_weather_day7 = image_weather_day7, image_weather_day8 = image_weather_day8,
                           image_weather_day9 = image_weather_day9)

@app.get("/update")
def update():
    today_weathe = today_weather.replace(",", " ")
    list_ = [date_, today_celcius, today_weathe, wind_kmh, humidity, dewpoint_celcius, pressure_barometric, uv_index, visibilty, moon_phase]
    return list_

@app.get("/update10")
def update10():
    day2[3] = day2[3].replace(",", " ")
    day3[3] = day2[3].replace(",", " ")
    day4[3] = day4[3].replace(",", " ")
    day5[3] = day5[3].replace(",", " ")
    day6[3] = day6[3].replace(",", " ")
    day7[3] = day7[3].replace(",", " ")
    day8[3] = day8[3].replace(",", " ")
    day9[3] = day9[3].replace(",", " ")
    list_2 = [day2, day3, day4, day5, day6, day7, day8, day9]
    return list_2

if __name__ == '__main__':
    app.run(debug=True)
