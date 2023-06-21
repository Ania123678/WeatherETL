# ETL pipeline for weather app
## Introduction:
The website showcases the up-to-date weather data in a user-friendly format.
The ETL pipeline enables the extraction, transformation, and loading of weather data for the app. Users can access accurate and timely weather information through the simple web interface.

## The ETL pipeline in the weather app repository consists of the following components:
- Web Scraping script: A module to extract weather information from a specific website. It collects and processes the relevant data points.
  
- DAG Management with Airflow:A file that manages task scheduling and dependencies using Airflow. It ensures the ETL process runs smoothly.
  
- Webpage using Flask and Bootstrap:
Built with Flask, a Python web framework, and Bootstrap for a clean interface. It displays the weather information retrieved from the web scraping module.

- Test using pytest

## How to launch project:
### - Make requirements.txt file with this requirements:

bs4==0.0.1

wordninja==2.0.0

html5lib==1.1

numpy==1.21.6

pytest==7.3.1

### - Create a Dockerfile:

FROM apache/airflow:2.5.2

COPY requirements.txt /requirements.txt

RUN pip install --user --upgrade pip

RUN pip install --no-cache-dir --user -r /requirements.txt

### - Define services in a Compose file

### - Build and run your app with Compose
From your project directory, start up your application by running "docker compose up"


## Webpage:
A website that displays weather information based on the webscraped data:
![Bez tytułu](https://user-images.githubusercontent.com/102367840/232322329-bbd277f2-73e7-48d1-92b6-d06e399204ac.png)
