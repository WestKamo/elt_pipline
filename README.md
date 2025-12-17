# 🏭 The Containerized Data Factory

**A Full-Stack ELT Pipeline built with Docker, PostgreSQL, dbt, and Apache Airflow.**

Welcome to my data engineering playground! What started as a simple Python script to move data between two databases has evolved into a robust, orchestrated data platform. I built this to master the fundamentals of modern data infrastructure—handling everything from raw container networking to complex transformation logic.

---

## 🚀 What's Under the Hood?

This isn't just a copy-paste project. It is a fully integrated stack simulating a real-world data environment.

* **🐳 Docker & Docker Compose:** The backbone. Everything runs in isolated containers with a custom internal network (`elt_network`).
* **🐘 PostgreSQL (x2):** A "Source" DB (simulating a production app) and a "Destination" DB (our Data Warehouse).
* **🐍 Python:** A custom ELT script acting as the "delivery driver," extracting raw data and loading it into the warehouse.
* **✨ dbt (Data Build Tool):** The transformation layer. Once data arrives, dbt cleans it, joins tables, and runs tests to ensure quality.
* **🌬️ Apache Airflow:** The orchestrator. Instead of fragile cron jobs, I use Airflow DAGs and `DockerOperators` to manage dependencies and schedule the entire workflow.

---

## 🛠️ The Architecture

### 1. Extraction & Loading (EL)
* A custom Python script waits for the `source_db` to initialize.
* It uses `pg_dump` and `psql` to stream data directly to the `destination_db`.
* **Challenge Solved:** Optimized for WSL2 performance using **Named Volumes** to prevent I/O bottlenecks and timeouts.

### 2. Transformation (T)
* **dbt** takes over once the data lands.
* Configured `sources.yml` to treat the destination DB as the source of truth (solving cross-database querying limitations).
* Includes custom SQL models (`stg_users`, `film_ratings_summary`), generic tests, and Jinja macros for reusable logic.

### 3. Orchestration
* **Airflow** manages the lifecycle.
* It spins up the Python container ➡️ Waits for success ➡️ Spins up the dbt container.
* If any step fails, the pipeline stops and alerts (no more silent failures!).

---

## 📂 Repository Structure

```text
custom-elt-project-main/
├── dags/                  # Airflow DAGs (The "Manager" scripts)
│   └── elt_dag.py         # Defines the task order: Python Script -> dbt
├── custom_postgres/       # The dbt Project (The "Chef")
│   ├── models/            # SQL Transformations (Staging & Marts)
│   ├── macros/            # Reusable SQL functions
│   └── profiles.yml       # Connection configs
├── elt_script/            # The Extraction Script (The "Driver")
│   ├── Dockerfile         # Custom image definition
│   └── elt_script.py      # The logic to move data
├── source_db_init/        # Initial seed data for the source DB
└── docker-compose.yaml    # The Master Blueprint
