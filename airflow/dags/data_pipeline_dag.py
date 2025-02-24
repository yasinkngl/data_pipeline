from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.data_ingestion import fetch_data
from src.data_cleaning import clean_data
from src.db_integration import insert_into_postgres, insert_into_mongodb

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # Change start_date to a past date for testing:
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('data_pipeline_dag', default_args=default_args, schedule_interval='@daily')

def ingestion_task(**context):
    data = fetch_data()
    # Optionally log the data length
    print(f"Fetched {len(data.get('docs', [])) if data else 0} records.")
    context['ti'].xcom_push(key='raw_data', value=data)

def cleaning_task(**context):
    ti = context['ti']
    raw_data = ti.xcom_pull(key='raw_data', task_ids='fetch_data_task')
    cleaned = clean_data(raw_data)
    print(f"Cleaned data contains {len(cleaned) if cleaned else 0} records.")
    ti.xcom_push(key='cleaned_data', value=cleaned)

def insert_postgres_task(**context):
    ti = context['ti']
    cleaned_data = ti.xcom_pull(key='cleaned_data', task_ids='clean_data_task')
    insert_into_postgres(cleaned_data)
    print("Data inserted into PostgreSQL.")

def insert_mongodb_task(**context):
    ti = context['ti']
    cleaned_data = ti.xcom_pull(key='cleaned_data', task_ids='clean_data_task')
    insert_into_mongodb(cleaned_data)
    print("Data inserted into MongoDB.")

def debug_task(**context):
    ti = context['ti']
    cleaned_data = ti.xcom_pull(key='cleaned_data', task_ids='clean_data_task')
    # Print a sample of the data (first 3 records)
    print("Sample of cleaned data:", cleaned_data[:3] if cleaned_data else "No data")

debug_operator = PythonOperator(
    task_id='debug_task',
    python_callable=debug_task,
    provide_context=True,
    dag=dag
)

fetch_data_task = PythonOperator(
    task_id='fetch_data_task',
    python_callable=ingestion_task,
    provide_context=True,
    dag=dag
)

clean_data_task = PythonOperator(
    task_id='clean_data_task',
    python_callable=cleaning_task,
    provide_context=True,
    dag=dag
)

insert_postgres = PythonOperator(
    task_id='insert_postgres_task',
    python_callable=insert_postgres_task,
    provide_context=True,
    dag=dag
)

insert_mongodb = PythonOperator(
    task_id='insert_mongodb_task',
    python_callable=insert_mongodb_task,
    provide_context=True,
    dag=dag
)


# Define task dependencies:
fetch_data_task >> clean_data_task >> debug_operator >> [insert_postgres, insert_mongodb]
