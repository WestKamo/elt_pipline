FROM ghcr.io/dbt-labs/dbt-postgres:1.7.2

WORKDIR /usr/app

# Copy project files
COPY . .

# Install dependencies if any
RUN dbt deps
