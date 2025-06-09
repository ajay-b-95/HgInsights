# HgInsights Assinment

Tools used:
1) Orchestraton of pipeline: Apache arflow (Open Source)
2) Transfromation ETL: Python Pandas & diff Lib
3) Infra can be set up in codespace
4) DockerFile can be run on the given files and reuirements
5) Sorce and Sink will be stored in the Postgre relational DB which can be integrated via metabase


# ELT Pipeline with Airflow, PostgreSQL, and Metabase

- `data/`: Contains source CSV dataset
- `etl/`: Python-based transformation logic (handling missing values, Bai Checks , KPIS, anonymizing PII)
- `dags/`: Airflow DAG for orchestrating ELT hourly
- `docker-compose.yml`: Launches all components in containers

1. Clone the repository

```bash
git clone https://github.com/your-username/elt-pipeline-demo.git
cd elt-pipeline-demo

Open codespace and run the dockerfile
with
docker-compose up --build
services with Ports can be vieved and changed

