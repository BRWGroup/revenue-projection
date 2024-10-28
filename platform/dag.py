import os
import datetime
from dotenv import load_dotenv

load_dotenv()

from ecp_cdk.utils import load_spec
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

# Load config
spec = load_spec(os.environ("PRODUCT_SPEC_PATH"))

with DAG(
    dag_id=spec["info"]["title"],
    start_date=datetime.strptime(
        spec["tranform"]["schedule"]["start_date"], "%Y-%m-%d"
    ),
    schedule=spec["tranform"]["schedule"]["cron"],
):
    task = DockerOperator(
        task_id=spec["info"]["title"],
        cpus=["tranform"]["cpu"],
        image='Dockerfile',
        container_name=spec["info"]["title"],
        api_version='auto',
        auto_remove=True,
        docker_url='tcp://docker-proxy:2375',
        network_mode='container:spark-master',
        tty=True,
        xcom_all=False,
        mount_tmp_dir=False,
        environment={
        'SPARK_APPLICATION_ARGS': '{{ task_instance.xcom_pull(task_ids="store_prices") }}'
        }
    )
