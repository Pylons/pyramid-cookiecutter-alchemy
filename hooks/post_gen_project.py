import os
import subprocess
import sys

from textwrap import dedent

WIN = sys.platform.startswith('win')

venv = 'env'
if WIN:
    venv_cmd = 'py -3 -m venv'
    venv_bin = os.path.join(venv, 'Scripts')
else:
    venv_cmd = 'python3 -m venv'
    venv_bin = os.path.join(venv, 'bin')

vars = dict(
    separator='=' * 79,
    venv=venv,
    venv_cmd=venv_cmd,
    pip_cmd=os.path.join(venv_bin, 'pip'),
    pytest_cmd=os.path.join(venv_bin, 'pytest'),
    pserve_cmd=os.path.join(venv_bin, 'pserve'),
    alembic_cmd=os.path.join(venv_bin, 'alembic'),
    init_cmd=os.path.join(venv_bin, 'initialize_{{ cookiecutter.repo_name }}_db'),
)
msg = dedent(
    """
    %(separator)s
    Documentation: https://docs.pylonsproject.org/projects/pyramid/en/latest/
    Tutorials:     https://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
    Twitter:       https://twitter.com/PylonsProject
    Mailing List:  https://groups.google.com/forum/#!forum/pylons-discuss
    Welcome to Pyramid.  Sorry for the convenience.
    %(separator)s

    Change directory into your newly created project.
        cd {{ cookiecutter.repo_name }}

    Create a Python virtual environment.
        %(venv_cmd)s %(venv)s

    Upgrade packaging tools.
        %(pip_cmd)s install --upgrade pip setuptools

    Install the project in editable mode with its testing requirements.
        %(pip_cmd)s install -e ".[testing]"

    Initialize the database.

        # This cookiecutter provides support for initializing the database
        # with migrations through alembic.
        #
        # Initialize the database with migrations through alembic:
        # First use alembic to generate revisions.
        %(alembic_cmd)s -c development.ini revision --autogenerate -m "init"
        # upgrade to that revision:
        %(alembic_cmd)s -c development.ini upgrade head
        # Later you can run database migrations.

    Run your project's tests.
        %(pytest_cmd)s

    Run your project.
        %(pserve_cmd)s development.ini
    """ % vars)
print(msg)
