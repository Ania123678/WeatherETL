import pytest
import bs4 as BeautifulSoup
from airflow.providers.postgres.hooks.postgres import PostgresHook

from extract import extract_data
from transform import transform_data
from load import load_data


from variables import URL_WEATHER, POSTGRES_CONN_ID, SCHEMA
url = URL_WEATHER
response = extract_data(url)

def test_web_scraper_response():
    response = extract_data(url)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"
   
def test_web_scraper_content():
    response = extract_data(url)
    assert response.text != None

def test_response_soup():
    soup = BeautifulSoup.BeautifulSoup(response.text, 'html5lib')
    assert soup.find('div', {'class':'CurrentConditions--primary--2DOqs'}) != None
    assert soup.find_all('div', {'class':'WeatherDetailsListItem--wxData--kK35q'}) != None

def test_postgres_hook():

    hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID, schema = SCHEMA)
    conn = hook.get_conn()
    assert conn is not None

    query = "SELECT * FROM weather"
    result = hook.get_records(query)
    assert isinstance(result, list)






