{{ cookiecutter.repo_name }}
===============================

Getting Started
---------------

- Create a Python virtual environment:

    python3 -m venv $VENV

- Install the project in editable mode:

    $VENV/bin/pip install -e ".[testing]"

- Configure the database:

    $VENV/bin/initialize_{{ cookiecutter.repo_name }}_db development.ini

- Start the server:

    $VENV/bin/pserve development.ini
