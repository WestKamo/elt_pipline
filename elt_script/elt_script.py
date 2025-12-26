import subprocess
import time

def wait_for_postgres(host, max_retries=5, delay_seconds=5):
    retries = 0
    while retries < max_retries:
        try:
            result = subprocess.run(
                ["pg_isready", "-h", host], check=True, capture_output=True, text=True)
            if "accepting connections" in result.stdout:
                print("Successfully connected to PostgreSQL!")
                return True
        except subprocess.CalledProcessError as e:
            print(f"Error connecting to PostgreSQL: {e}")
            retries += 1
            time.sleep(delay_seconds)
    return False

if not wait_for_postgres(host="source_postgres"):
    exit(1)

source_config = {'dbname': 'source_db', 'user': 'postgres', 'password': 'secret', 'host': 'source_postgres'}
destination_config = {'dbname': 'destination_db', 'user': 'postgres', 'password': 'secret', 'host': 'destination_postgres'}

print("Dumping source database...")
subprocess.run(['pg_dump', '-h', source_config['host'], '-U', source_config['user'], '-d', source_config['dbname'], '-f', 'data_dump.sql', '-w'], env=dict(PGPASSWORD=source_config['password']), check=True)

print("Loading into destination...")
subprocess.run(['psql', '-h', destination_config['host'], '-U', destination_config['user'], '-d', destination_config['dbname'], '-a', '-f', 'data_dump.sql'], env=dict(PGPASSWORD=destination_config['password']), check=True)
