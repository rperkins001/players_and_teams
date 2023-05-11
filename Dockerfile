FROM python:3.9-bullseye

# Set the working directory in the image to /pitchrite
WORKDIR /players_and_teams

# Copy the required files from the host machine to the image
COPY . .

# Install the required libraries
RUN apt-get update && \
    apt-get install -y python3-dev libcurl4-openssl-dev && \
    pip install --upgrade pip --no-cache-dir && \
    pip install --no-cache-dir -r requirements.txt
# Set the environment variable for Django
ENV DJANGO_SETTINGS_MODULE=players_and_teams.settings

# Expose the port for Django
EXPOSE 8000

# Define the command to run when the container starts
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]