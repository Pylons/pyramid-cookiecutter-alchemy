import os
import sys

from pyramid.paster import get_appsettings, setup_logging
from sqlalchemy.exc import OperationalError
import transaction

from .. import models
from ..models import get_engine, get_session_factory, get_tm_session


def setup_models(dbsession):
    model = models.MyModel(name='one', value=1)
    dbsession.add(model)


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = get_engine(settings)
    session_factory = get_session_factory(engine)
    tm = transaction.TransactionManager(explicit=True)

    try:
        with tm:
            dbsession = get_tm_session(session_factory, tm)
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            ''')
