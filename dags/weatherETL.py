import requests
import bs4 as BeautifulSoup
import math
import wordninja
import datetime
from airflow.providers.postgres.hooks.postgres import PostgresHook

headers = {}
url_weather_today = ""
response = requests.get(url_weather_today, headers=headers)
print(response.status_code)
soup = BeautifulSoup.BeautifulSoup(response.text, 'html5lib')


def today_Weather(soup):

  
  today = datetime.datetime.now().date()

  spans = soup.find('div', {'class':'CurrentConditions--primary--2DOqs'})
  text = []
  for span in spans:
    text.append(span.text)

  temp = text[0]
  temp = temp.replace('°','')
  today_celcius = int((int(temp) - 32) * (5/9))


  today_weather = wordninja.split(text[1])
  today_weather = ",".join(today_weather)


  spans = soup.find_all('div', {'class':'WeatherDetailsListItem--wxData--kK35q'})
  p = []
  for span in spans:
    p.append(span.text)
  high_low = p[0]

  wind_mph = p[1].replace("Wind Direction", "")
  wind_kmh = int(int(wind_mph[0:2]) * 1.609344)

  humidity = p[2].replace("%", "")
  dewpoint_fahrenheit  = p[3].replace("°", "")
  dewpoint_celcius = int((int(dewpoint_fahrenheit) - 32) * (5/9))


  pressure_millibar = p[4]
  pressure_millibar = wordninja.split(pressure_millibar)
  if 'Arrow' in pressure_millibar:
    pressure_millibar.remove('Arrow')
  if 'Down' in pressure_millibar:
    pressure_millibar.remove('Down')
  if 'Up' in pressure_millibar:
    pressure_millibar.remove('Up')

  pressure_millibar = str(pressure_millibar[0]) + "." + str(pressure_millibar[1])
  pressure_barometric = int(float(pressure_millibar) * 33.863)
  uv_index = p[5]
  visibilty = math.ceil(int(p[6].replace("mi", "")) * 1.609344)
  moon_phase = p[7]

  pg_hook = PostgresHook(postgres_conn_id='', schema = '')
  connection = pg_hook.get_conn()
  cursor = connection.cursor()

  query = "INSERT INTO weather(weather_day, temperature, weather, wind, humidity, dewpoint, pressure, uv_index, visibility, moon_phase) VALUES (%s, %s, %s , %s, %s, %s, %s, %s , %s, %s)"
  cursor.execute(query, (today, today_celcius, today_weather, wind_kmh, humidity, dewpoint_celcius, pressure_barometric, uv_index, visibilty, moon_phase))
  connection.commit()

  cursor.close()
  connection.close()

def startETL():
  today_Weather(soup)
 

