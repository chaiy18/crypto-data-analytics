# 🚀 Crypto Data Analytics

## 📌 Overview

This project demonstrates an end-to-end data engineering pipeline that ingests real-time cryptocurrency data from an external API, processes it using PySpark, and orchestrates workflows using Apache Airflow.

The pipeline is designed with modular ETL components, configuration-driven logic, and logging for observability — closely resembling production-grade data pipelines.

---

## ⚙️ Tech Stack

* Python
* PySpark (Distributed Processing)
* Apache Airflow (Workflow Orchestration)
* Pandas (Lightweight Processing)
* YAML (Configuration Management)
* Logging (Observability)

---

## 🧱 Architecture

```
CoinGecko API
      ↓
Ingestion Layer (Python API Calls)
      ↓
Raw Storage (CSV)
      ↓
Transformation Layer (PySpark)
      ↓
Processed Storage (Parquet)
      ↓
Aggregation Layer (Metrics)
      ↓
Airflow (Workflow Orchestration)
```

## 📂 Project Structure

```
crypto-data-analytics/
│
├── dags/                  # Airflow DAG definitions
│   └── crypto_dag.py
│
├── jobs/                  # ETL jobs
│   ├── ingestion.py
│   ├── transformation.py
│   └── aggregation.py
│
├── pipelines/             # Pipeline orchestration logic
│   └── batch_pipeline.py
│
├── utils/                 # Utility modules
│   ├── spark_session.py
│   └── logger.py
│
├── config/
│   └── config.yaml        # Centralized configuration
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── aggregated/
│
├── main.py                # Local pipeline execution
├── requirements.txt
└── README.md
```

---

## 🔄 Pipeline Flow

### 🔹 1. Ingestion

* Fetches real-time cryptocurrency prices from CoinGecko API
* Stores raw data in CSV format
* Config-driven coin selection

### 🔹 2. Transformation

* Reads raw data using PySpark
* Applies data cleaning and validation
* Converts data into optimized Parquet format

### 🔹 3. Aggregation

* Computes average price per cryptocurrency
* Generates analytical dataset for downstream use

### 🔹 4. Orchestration

* Airflow schedules and executes the pipeline
* Supports retries and monitoring

---

## ▶️ Running Locally

```bash
python main.py
```

---

## 🌪️ Running with Airflow

### 1. Start Airflow Services

```bash
airflow webserver --port 8081
airflow scheduler
```

### 2. Access UI

```
http://localhost:8081
```

### 3. Trigger Pipeline

* Enable DAG: `crypto_data_analytics`
* Click ▶ Run

---

## 📊 Output

* **Raw Layer** → CSV files (`data/raw/`)
* **Processed Layer** → Parquet files (`data/processed/`)
* **Aggregated Layer** → Average price metrics (`data/aggregated/`)

---

## 🔥 Key Features

* Modular ETL architecture
* Config-driven pipeline (YAML)
* Structured logging for debugging
* PySpark-based scalable transformations
* Airflow-based orchestration
* Clean separation of concerns

---

## 🧠 What This Project Demonstrates

* Building production-style ETL pipelines
* Integrating external APIs into data workflows
* Using Spark for scalable data processing
* Orchestrating pipelines using Airflow
* Managing configurations and environments

---

## 🚀 Future Enhancements

* Integrate cloud storage (AWS S3 / GCS)
* Add Docker-based deployment
* Implement streaming pipeline (Kafka + Spark Streaming)
* Add monitoring and alerting (Airflow alerts / Prometheus)
* Store results in a data warehouse (BigQuery / Snowflake)

---
