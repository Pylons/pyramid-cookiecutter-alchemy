{{ cookiecutter.repo_name }}
===============================

Getting Started
---------------

- cd <directory containing this file>

  - $VENV/bin/pip install -e .

  - $VENV/bin/initialize_{{ cookiecutter.repo_name }}_db development.ini

  - $VENV/bin/pserve development.ini
