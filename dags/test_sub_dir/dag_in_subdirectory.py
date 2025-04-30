from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


def hello_from_subdir():
  print("Hello from a DAG inside a subdirectory!")


with DAG(
    dag_id='dag_in_subdirectory',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@once',
    catchup=False,
    description='DAG placed inside a subdirectory to test scanning',
) as dag:

  task = PythonOperator(
      task_id='print_hello',
      python_callable=hello_from_subdir,
  )
