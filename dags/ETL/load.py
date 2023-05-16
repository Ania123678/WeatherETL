from airflow.providers.postgres.hooks.postgres import PostgresHook
from transform import transform_data
import sys, os
sys.path.append(os.path.dirname(sys.path[0]))

from variables import POSTGRES_CONN_ID, SCHEMA
today, temperature_celsius, today_weather, wind_kmh, humidity, dewpoint, pressure_barometric, uv_index, visibilty, moon_phase = transform_data()


def load_data(today, today_celcius, today_weather, wind_kmh, humidity, dewpoint_celcius, pressure_barometric, uv_index, visibilty, moon_phase):
  pg_hook = PostgresHook(postgres_conn_id= POSTGRES_CONN_ID, schema = SCHEMA)
  connection = pg_hook.get_conn()
  cursor = connection.cursor()

  query = "INSERT INTO weather(weather_day, temperature, weather, wind, humidity, dewpoint, pressure, uv_index, visibility, moon_phase) VALUES (%s, %s, %s , %s, %s, %s, %s, %s , %s, %s)"
  cursor.execute(query, (today, today_celcius, today_weather, wind_kmh, humidity, dewpoint_celcius, pressure_barometric, uv_index, visibilty, moon_phase))
  connection.commit()

  cursor.close()
  connection.close()

