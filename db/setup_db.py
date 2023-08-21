from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from core.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = scoped_session(sessionmaker(bind=engine))
session()
