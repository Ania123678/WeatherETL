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

        date_ = weather_records[0][1]
        date_ = date_.strftime('%d %B')
        today_celcius = weather_records[0][2]
        today_weather = weather_records[0][3]
        wind_kmh = weather_records[0][4]
        humidity = weather_records[0][5]
        dewpoint_celcius = weather_records[0][6]
        pressure_barometric = weather_records[0][7]
        uv_index = weather_records[0][8]
        visibilty = weather_records[0][9]
        moon_phase = weather_records[0][10]

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
    
    return date_, today_celcius, today_weather, wind_kmh, humidity, dewpoint_celcius, pressure_barometric, uv_index, visibilty, moon_phase


