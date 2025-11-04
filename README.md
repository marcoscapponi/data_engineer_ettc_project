# ETTC Data Engineering Pipeline

End to end data pipeline for ETTC ecommerce dataset using AirFlow, Docker, PostgreSQL, and Power BI

## Project Overview

This project automates the ingestion, transformation, modeling, and visualization of ecommerce data using a modular Airflow DAG.

## DAG Architecture

```text
ETTC Airflow DAG
├── load_parquet_to_postgres
├── train_model
├── export_metrics
```

## Folder Structure

```text
  data_engineer_ettc_project/
├── dags/
├── scripts/
├── models/
├── metrics/
├── Dockerfile
├── docker-compose.yaml
├── .env
└── README.md
```

