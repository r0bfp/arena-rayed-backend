from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ



connection_url = engine.url.URL.create(
    drivername = 'cockroachdb',
    username   = environ.get('RAGE_DB_USER'),
    password   = environ.get('RAGE_DB_PASS'),
    database   = environ.get('RAGE_DB_NAME'),
    host       = environ.get('RAGE_DB_HOST'),
    port       = 26257,
    query      = {'sslmode': 'verify-full'}
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