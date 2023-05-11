# Teams and Players Django Application

This is a simple Django web application that tracks information on sports teams and the players on those teams.

## Features

- User authentication system
- Full CRUD operations on Teams and Players
- Assign Players to multiple Teams
- Dockerized setup for easy deployment

## Prerequisites

- Python 3.7 or higher
- Docker and Docker Compose

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/teams-and-players.git
    cd teams-and-players
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create the superuser and user accounts:

    ```bash
    python manage.py createsuperuser --email admin@endtoendinnovations.com --username admin
    python manage.py createuser --email user@endtoendinnovations.com --username user
    ```

6. Collect static files:

    ```bash
    python manage.py collectstatic
    ```

7. Run the application using Docker Compose:

    ```bash
    docker-compose up
    ```

8. Access the application at `http://localhost:8000` or your configured IP address and port.


# File System Diagram:

- .
    - Dockerfile
    - db.sqlite3
    - docker-compose.yml
    - manage.py
    - myenv
        - bin
        - include
        - lib
        - pyvenv.cfg
    - players_and_teams
        - __init__.py
        - asgi.py
        - settings.py
        - urls.py
        - wsgi.py
    - requirements.txt
    - static
        - admin
        - favicon.ico
        - img
    - staticfiles
        - admin
        - favicon.ico
        - img
    - team_tracker
        - __init__.py
        - admin.py
        - apps.py
        - context_processors.py
        - forms.py
        - migrations
        - models.py
        - tests.py
        - urls.py
        - views.py
    - templates
        - base.html
        - home.html
        - login.html
        - players
        - team
