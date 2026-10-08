from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/db_school'

engine = create_engine(DATABASE_URL)
SesseionLocal = sessionmaker(bind=engine)

Base = declarative_base()
