{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

Getting Started
---------------

- Change directory into your newly created project.

    cd {{ cookiecutter.repo_name }}

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Initialize the database.

    - This cookiecutter provides support for initializing the database either
    - (a) with migrations through alembic, or
    - (b) without migrations.
    
    - (a) Initialize the database with migrations through alembic:
    - First use alembic to generate revisions.

        env/bin/alembic -c development.ini revision --autogenerate -m "init"

    - upgrade to that revision:

        env/bin/alembic -c development.ini upgrade head
    
    - Later you can run database migrations.
    - Also there is commented code that can be used to
    - initialize the database directly to the latest revision.
    - {{cookiecutter.repo_name}}/scripts/initializedb.py
    
    - (b) Initialize the database without migrations:
        env/bin/initialize_{{cookiecutter.repo_name}}_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
