from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import db as cfg

# build db connection string
if cfg['env'] == 'local':
    db_uri = 'postgres+psycopg2://{}@{}:{}/{}'\
        .format(cfg['user'], cfg['host'], cfg['port'], cfg['db'])
else:
    db_uri = 'postgres+psycopg2://{}:{}@{}:{}/{}'\
        .format(cfg['user'], cfg['password'], cfg['host'], cfg['port'], cfg['db'])

# register db engine (in our case postgresql)
engine = create_engine(db_uri)

# instantiate a session, which retrieves a cnx from a cnx pool
# maintained by the engine
session = sessionmaker(bind=engine)
# sqlalchemy will check to see if a thread-local session exists
db_session = scoped_session(session)

# create base mapper from which our models will inherit
DeclarativeBase = declarative_base()
DeclarativeBase.query = db_session.query_property()


def init_db():
    """
    Used to run a one-off Docker container to seed the DB
    """
    import os, csv
    from modules.models import event, listing, order, user_session, user, venue
    
    # Create empty tables in DB
    DeclarativeBase.metadata.create_all(bind=engine)
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

    # Populate table data in DB
    tables = ['users', 'venues', 'events', 'listings'] # Must remain in this order for foreign key integrity
    for t in tables:
        csv_path = os.path.join(data_path, '{}.csv'.format(t))
        with open(csv_path, 'r') as f:
            # Get concatenated list of colnames from csv header
            reader = csv.reader(f)
            header = next(reader)
            colnames = ','.join(header)

            # Open a DB connection and copy data
            conn = engine.raw_connection()
            cursor = conn.cursor()
            cmd = 'COPY {}({}) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'.format(t, colnames, csv_path)
            cursor.copy_expert(cmd, f)
            conn.commit()
