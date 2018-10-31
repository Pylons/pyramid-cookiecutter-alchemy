============================
pyramid-cookiecutter-alchemy
============================

Deprecation notice
------------------

This cookiecutter has been deprecated in favor of the unified cookiecutter `pyramid-cookiecutter-starter <https://github.com/pylons/pyramid-cookiecutter-starter>`_ effective with the release of Pyramid 1.10.
``pyramid-cookiecutter-starter`` combines all features of ``pyramid-cookiecutter-alchemy`` and ``pyramid-cookiecutter-zodb``.
Please use `pyramid-cookiecutter-starter <https://github.com/pylons/pyramid-cookiecutter-starter>`_ instead of this one.
This cookiecutter may not receive further updates.

.. image:: https://travis-ci.org/Pylons/pyramid-cookiecutter-alchemy.png?branch=latest
        :target: https://travis-ci.org/Pylons/pyramid-cookiecutter-alchemy
        :alt: latest Travis CI Status

A Cookiecutter (project template) for creating a Pyramid project using SQLite for persistent storage, SQLAlchemy for an ORM, Alembic for database migrations, URL dispatch for routing, and Jinja2 for templating.

Requirements
------------

* Python 2.7 or 3.4+
* `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Versions
--------

This cookiecutter has several branches to support new features in Pyramid or avoid incompatibilities.

* ``latest`` aligns with the latest stable release of Pyramid, and is the default branch on GitHub.
* ``master`` aligns with the ``master`` branch of Pyramid, and is where development takes place.
* ``x.y-branch`` aligns with the ``x.y-branch`` branch of Pyramid.


Usage
-----

1.  Generate a Pyramid project, following the prompts from the command.

    .. code-block:: bash

        $ cookiecutter gh:Pylons/pyramid-cookiecutter-alchemy

    Optionally append a specific branch checkout to the command:

    .. code-block:: bash

        $ cookiecutter gh:Pylons/pyramid-cookiecutter-alchemy --checkout master

2.  Finish configuring the project by creating a virtual environment and installing your new project. These steps are output as part of the cookiecutter command above and are slightly different for Windows.

    .. code-block:: bash

        # Change directory into your newly created project.
        $ cd myproj
        # Create a virtual environment...
        $ python3 -m venv env
        # ...where we upgrade packaging tools...
        $ env/bin/pip install --upgrade pip setuptools
        # ...and into which we install our project and its testing requirements.
        $ env/bin/pip install -e ".[testing]"

3.  Initialize and upgrade the database using Alembic.

    .. code-block:: bash

        # Generate your first revision.
        $ env/bin/alembic -c development.ini revision --autogenerate -m "init"
        # Upgrade to that revision.
        $ env/bin/alembic -c development.ini upgrade head

4.  Load default data into the database using a script.

    .. code-block:: bash

        $ env/bin/initialize_tutorial_db development.ini

5.  Run your project's tests.

    .. code-block:: bash

        $ env/bin/pytest

6.  Run your project.

    .. code-block:: bash

        $ env/bin/pserve development.ini
