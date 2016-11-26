============================
pyramid-cookiecutter-alchemy
============================

.. image:: https://travis-ci.org/Pylons/pyramid-cookiecutter-alchemy.png?branch=master
        :target: https://travis-ci.org/Pylons/pyramid-cookiecutter-alchemy
        :alt: Master Travis CI Status

A cookiecutter (project template) for creating a Pyramid project using SQLite
as persistent storage, SQLAlchemy as an ORM, URL dispatch for routing, and
Jinja2 for templating.

Requirements
------------

* Python 2.7 or 3.4+
* `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Usage
-----

1. Generate a Pyramid project.

.. code-block:: bash

    $ cookiecutter https://github.com/Pylons/pyramid-cookiecutter-alchemy

2. Finish configuring the project by creating a virtual environment and
   installing your new project. These steps are output as part of the
   cookiecutter command above and are slightly different for Windows.

.. code-block:: bash

    $ cd myproj
    $ python3 -m venv env
    $ env/bin/pip install -e ".[testing]"

3. Configure the database.

.. code-block:: bash

    $ env/bin/initialize_myproj_db development.ini

4. Run your project.

.. code-block:: bash

    $ env/bin/pserve development.ini
