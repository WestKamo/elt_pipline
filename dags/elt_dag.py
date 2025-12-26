from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker_operator import DockerOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'elt_and_dbt_pipeline',
    default_args=default_args,
    description='Runs ELT script then dbt transformations',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    t1 = DockerOperator(
        task_id='run_elt_script',
        image='elt_script_v1:latest',
        container_name='elt_script_runner',
        api_version='auto',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='elt_network',
        environment={
            'POSTGRES_USER': 'postgres',
            'POSTGRES_PASSWORD': 'secret'
        }
    )

    t2 = DockerOperator(
        task_id='run_dbt',
        image='dbt_custom_v1:latest',
        container_name='dbt_runner',
        api_version='auto',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='elt_network',
        command='dbt run --profiles-dir /usr/app'
    )

    t1 >> t2
