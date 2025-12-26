FROM apache/airflow:2.7.1
USER root
RUN apt-get update &&     apt-get install -y gcc python3-dev
USER airflow
RUN pip install apache-airflow-providers-docker
