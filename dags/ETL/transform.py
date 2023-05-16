import requests
import bs4 as BeautifulSoup
import math 
import wordninja
import datetime

import sys, os
sys.path.append(os.path.dirname(sys.path[0]))

from variables import URL_WEATHER

from extract import extract_data
response = extract_data(URL_WEATHER)

def transform_data():

  soup = BeautifulSoup.BeautifulSoup(response.text, 'html5lib')
  today = datetime.datetime.now().date()

  spans = soup.find('div', {'class':'CurrentConditions--primary--2DOqs'})
  data = []
  for span in spans:
    data.append(span.text)

  temperature_fahrenheit = int(data[0].replace('°',''))
  temperature_celsius = round((temperature_fahrenheit - 32) * 5/9)
  today_weather = today_weather = ",".join(wordninja.split(data[1]))

  spans = soup.find_all('div', {'class':'WeatherDetailsListItem--wxData--kK35q'})
  data2 = []
  for span in spans:
    data2.append(span.text)

  wind_mph = data2[1].replace("Wind Direction", "")
  wind_kmh = round(int(wind_mph[0:2]) * 1.609344)
  humidity = int(data2[2].replace("%", ""))
  dewpoint_ = data2[3].replace("°", "")
  dewpoint = round((int(dewpoint_) - 32) * (5/9))

  pressure_millibar = wordninja.split(data2[4])
  pressure_millibar = [p for p in pressure_millibar if p not in {'Arrow', 'Down', 'Up'}]
 
  pressure_millibar = str(pressure_millibar[0]) + "." + str(pressure_millibar[1])
  pressure_barometric = int(float(pressure_millibar) * 33.863)
  uv_index = data2[5]
  visibilty = math.ceil(int(data2[6].replace("mi", "")) * 1.609344)
  moon_phase = data2[7]

  return today, temperature_celsius, today_weather, wind_kmh, humidity, dewpoint, pressure_barometric, uv_index, visibilty, moon_phase