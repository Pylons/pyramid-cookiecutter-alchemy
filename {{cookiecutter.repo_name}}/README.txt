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

- Migrate the database using Alembic.

    - Generate revisions.

        env/bin/alembic -c development.ini revision --autogenerate -m "init"

    - Upgrade to that revision.

        env/bin/alembic -c development.ini upgrade head
    
    - Later you can run database migrations.

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
