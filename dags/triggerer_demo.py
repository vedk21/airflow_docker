from datetime import datetime, timedelta

import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.time_sensor import TimeSensorAsync

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='triggerer_demo',
    default_args=default_args,
    description='Demo of deferrable TimeSensorAsync + Triggerer',
    start_date=datetime(2025, 4, 30, tzinfo=pendulum.UTC),
    schedule_interval=None,
    catchup=False,
    tags=['example'],
) as dag:

  # 1. Runs immediately
  start = BashOperator(
      task_id='say_hello',
      bash_command='echo "Hello from the webserver at $(date)"',
  )

  # 2. Deferrable sensor: wait exactly one minute from now
  wait_one_minute = TimeSensorAsync(
      task_id='wait_one_minute',
      target_time=(pendulum.now('UTC') + timedelta(minutes=1)).time(),
  )

  # 3. Runs after the sensor fires
  after_wait = BashOperator(
      task_id='after_wait',
      bash_command='echo "Wait is over at $(date)"',
  )

  start >> wait_one_minute >> after_wait
