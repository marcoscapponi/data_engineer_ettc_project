from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'goyo',
    'start_date': datetime(2025, 10, 29),
    'retries': 1,
}

dag = DAG(
    dag_id='ettc_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='ETTC Pipeline DAG for synthetic ecommerce data'
)

def run_script(script_name):
    os.system(f'python {script_name}')

load_task = PythonOperator(
    task_id='load_parquet_to_postgres',
    python_callable=lambda: run_script("scripts/load_data.py"),
    dag=dag
)

train_task = PythonOperator(
    task_id='train_model',
    python_callable=lambda: run_script("scripts/train_model.py"),
    dag=dag
)

export_task = PythonOperator(
    task_id='export_metrics',
    python_callable=lambda: run_script("scripts/export_metrics.py"),
    dag=dag
)

load_task >> train_task >> export_task