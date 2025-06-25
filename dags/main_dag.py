from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import boto3

def start_glue_job(job_name):
    glue = boto3.client("glue", region_name="eu-west-1")
    glue.start_job_run(JobName=job_name)

with DAG("iceberg_pipeline",
         start_date=datetime(2023, 1, 1),
         schedule_interval="@daily",
         catchup=False) as dag:

    ingest = PythonOperator(
        task_id="ingest_data",
        python_callable=start_glue_job,
        op_kwargs={"job_name": "job_ingest"},
    )

    transform = PythonOperator(
        task_id="transform_and_write_iceberg",
        python_callable=start_glue_job,
        op_kwargs={"job_name": "job_transform"},
    )

    ingest >> transform