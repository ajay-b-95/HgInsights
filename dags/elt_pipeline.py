from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

dag = DAG(
    'elt_hourly_pipeline',
    schedule_interval='@hourly',
    start_date=days_ago(1),
    catchup=False,
    default_args={'retries': 1, 'retry_delay': timedelta(minutes=5)}
)

extract = BashOperator(
    task_id='load_csv',
    bash_command='psql -h postgres -U postgres -d postgres -c "\\copy staging.customers FROM \'/data/telecom_churn.csv\' DELIMITER \',\' CSV HEADER;"',
    dag=dag
)

transform = BashOperator(
    task_id='transform_load',
    bash_command='python3 /etl/transform.py',
    dag=dag
)

extract >> transform
