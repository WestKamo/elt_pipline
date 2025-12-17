🏭 The Containerized Data Factory
A Full-Stack ELT Pipeline built with Docker, PostgreSQL, dbt, and Apache Airflow.

Welcome to my data engineering playground! What started as a simple python script to move data between two databases has evolved into a robust, orchestrated data platform. I built this to master the fundamentals of modern data infrastructure—handling everything from raw container networking to complex transformation logic.

🚀 What's Under the Hood?
This isn't just a copy-paste project. It's a fully integrated stack simulating a real-world data environment.

🐳 Docker & Docker Compose: The backbone. Everything runs in isolated containers with a custom internal network (elt_network).

🐘 PostgreSQL (x2): A "Source" DB (simulating a production app) and a "Destination" DB (our Data Warehouse).

🐍 Python: A custom ELT script acting as the "delivery driver," extracting raw data and loading it into the warehouse.

✨ dbt (Data Build Tool): The transformation layer. Once data arrives, dbt cleans it, joins tables, and runs tests to ensure quality.

🌬️ Apache Airflow: The orchestrator. Instead of fragile cron jobs, I use Airflow DAGs and DockerOperators to manage dependencies and schedule the entire workflow.

🛠️ The Architecture
Extraction & Loading (EL):

A custom Python script waits for the source_db to initialize.

It uses pg_dump and psql to stream data directly to the destination_db.

Challenge Solved: Optimized for WSL2 performance using Named Volumes to prevent I/O bottlenecks and timeouts.

Transformation (T):

dbt takes over once the data lands.

configured sources.yml to treat the destination DB as the source of truth (solving cross-database querying limitations).

Includes custom SQL models (stg_users, film_ratings_summary), generic tests, and Jinja macros for reusable logic.

Orchestration:

Airflow manages the lifecycle.

It spins up the Python container ➡️ Waits for success ➡️ Spins up the dbt container.

If any step fails, the pipeline stops and alerts (no more silent failures!).

📂 Repository Structure
Plaintext

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
⚡ How to Run It
Prerequisites: Docker and Docker Compose.

Clone the repo:

Bash

git clone <your-repo-url>
cd custom-elt-project-main
The "WSL Hack" (If you are on Windows/WSL2): Airflow needs permission to talk to the Docker daemon.

Bash

sudo chmod 666 /var/run/docker.sock
Launch the Stack: Build the images and spin up the containers.

Bash

docker-compose up -d --build
Access the Airflow UI:

Go to: http://localhost:8080

User: airflow | Pass: airflow

Turn the toggle ON for elt_and_dbt_pipeline and click the Play button.

Watch the Magic: Go to the Graph View in Airflow. You'll see the system automatically:

✅ Provision a container to move data.

✅ Provision a container to run dbt transformations.

✅ Mark the job as "Success".

🧠 Key Learnings & Features
Race Conditions: Solved the "chicken and egg" problem where the script would run before the database was ready using Airflow dependencies (and Healthchecks).

Data Quality: Implemented dbt tests to catch null values and referential integrity issues before they hit the dashboard.

Infrastructure as Code: The entire environment—from database credentials to Airflow connections—is defined in code, making it reproducible on any machine.

Built with ❤️ and a lot of coffee by [Phindile Ivy].
