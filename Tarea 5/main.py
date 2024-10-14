from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

TAGS = ['PythonDataFlow']
DAG_ID = "A1"
DAG_DESCRIPTION = """Actividad1_Airflow"""
DAG_SCHEDULE = "0 9 * * *"  # Every day at 9:00 AM
default_args = {
    "start_date": datetime(2024, 10, 13),  # Correct usage of datetime
}
retries = 4
retry_delay = timedelta(minutes=5)

def execute_task():
    hora_actual = datetime.now()
    print(hora_actual)

dag = DAG(
    dag_id=DAG_ID,
    description=DAG_DESCRIPTION,
    catchup=False,
    schedule=DAG_SCHEDULE,
    max_active_runs=1,
    dagrun_timeout=timedelta(seconds=200000),
    default_args=default_args,
    tags=TAGS
)

with dag:
    start_task = EmptyOperator(
        task_id="inicia_proceso"
    )

    end_task = EmptyOperator(
        task_id="finaliza_proceso"
    )

    first_task = PythonOperator(
        task_id="first_task",
        python_callable=execute_task,
        retries=retries,
        retry_delay=retry_delay
    )

start_task >> first_task >> end_task
