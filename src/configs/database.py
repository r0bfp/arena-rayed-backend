from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ


username = environ.get('RAGE_DB_USER')
password = environ.get('RAGE_DB_PASS')
hostname = environ.get('RAGE_DB_HOST')
database = environ.get('RAGE_DB_NAME')
unix_socket_path = environ.get('UNIX_SOCKET_PATH')

if unix_socket_path:
    connection_url = engine.url.URL.create(
        drivername="mysql+pymysql",
        username=username,
        password=password,
        database=database,
        query={"unix_socket": unix_socket_path},
    )
else:
    connection_url = engine.url.URL.create(
        drivername = 'mysql+pymysql',
        username   = username,
        password   = password,
        host       = hostname,
        database   = database,
        port       = 3306,
    )


engine = create_engine(connection_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def setup_database():
    Base.metadata.create_all(bind=engine)