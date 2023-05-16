from extract import extract_data
from transform import transform_data
from load import load_data

import sys,os 

sys.path.append(os.path.dirname(sys.path[0]))
from variables import URL_WEATHER


def startETL():
  response = extract_data(URL_WEATHER)
  print("Extracting data...")
  today, today_celcius, today_weather, wind_kmh, humidity, dewpoint, pressure_barometric, uv_index, visibilty, moon_phase = transform_data()
  print("Transforming data...")
  load_data(today, today_celcius, today_weather, wind_kmh, humidity, dewpoint, pressure_barometric, uv_index, visibilty, moon_phase)
  print("Loading data...")
 
