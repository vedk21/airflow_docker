from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define a function to print the current date and time


def print_current_datetime():
  print(f"Current date and time: {datetime.now()}")


# Define the DAG
dag = DAG(
    'print_date_dag',  # DAG name
    description='A simple DAG that prints the current date and time',
    schedule_interval='* * * * *',  # Run every minute
    start_date=datetime(2023, 1, 1),  # Start date for the DAG
    catchup=False,  # Skip any missed runs
)

# Define a task using the PythonOperator
task = PythonOperator(
    task_id='print_date_task',  # Task ID
    python_callable=print_current_datetime,  # Function to call
    dag=dag,  # DAG to associate with the task
)

# Set the task to run
task
