from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from datetime import timedelta
from weatherETL import startETL
import pendulum


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    default_args = default_args,
    dag_id = 'WeatherDAG',
    description = 'weather dag',
    start_date = pendulum.yesterday(),
    schedule_interval='@hourly',
    catchup = False,
    
) as dag:
    
    createTable = PostgresOperator(
    task_id='CreateTable',
    postgres_conn_id='postgres_localhost',
    sql='sql/schema.sql'
    )
    
    startETL = PythonOperator(
        task_id='GetWeatherData',
        python_callable=startETL
    )

    testETL = PythonOperator(
        task_id='Test',
        python_callable=test_postgres_hook
    )

    createTable >> testETL >> startETL