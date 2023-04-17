import psycopg2
import datetime
import random

def updateWeather():
    try:
        connection = psycopg2.connect(user="",
                                    password="",
                                    port="",
                                    database="")
        
        cursor = connection.cursor()

        query = "SELECT * FROM weather ORDER BY id DESC LIMIT 1;"
        cursor.execute(query)
    
        print('request number ' + str(random.randint(0,100)))
        weather_records = cursor.fetchall()
        print('id of row ' + str(weather_records[0][0]))

        weather_records = [i for sub in weather_records for i in sub]
        [id, date_, today_celcius, today_weather, wind_kmh, humidity, dewpoint_celcius, pressure_barometric, uv_index, visibilty, moon_phase] = [i for i in weather_records]
        date_ = date_.strftime('%d %B')
 
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
    
    return date_, today_celcius, today_weather, wind_kmh, humidity, dewpoint_celcius, pressure_barometric, uv_index, visibilty, moon_phase


