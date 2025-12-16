FROM python:3.8-slim

# Install PostgreSQL command-line tools
RUN apt-get update && apt-get install -y postgresql-client-15
#copy the bash script
COPY start.sh /app/start.sh

WORKDIR /app
# Copy the ELT script
COPY elt_script.py .

#set the time
RUN echo "0 3 * * * python/app/elt_script.py" |


# Set the default command to run the ELT script
CMD ["python", "elt_script.py"]
