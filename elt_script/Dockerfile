FROM python:3.8-slim

# Install PostgreSQL command-line tools
RUN apt-get update && apt-get install -y postgresql-client-15

WORKDIR /app

# Copy the ELT script
COPY elt_script.py .

# Command to run (Triggered by Airflow)
CMD ["python", "elt_script.py"]
