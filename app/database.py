from venv import create
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from .config import settings

# default template for SQL alchemy db string looks like this >>>
# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# if using SQLite, have to pass in additional parameter into engine below, = 
# connect_args={"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# everything up to above, is standard template for postgres SQL/API with fastAPI

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(host ='localhost', database='Project1', 
#             user='postgres', password='927f0RdwOOd', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was good!")
#         break
#     except Exception as error:
#         print('Connecting to db failed.')
#         print("Error:", error)
#         time.sleep(3)


