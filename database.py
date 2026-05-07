from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

database_url = ("sqlite:///./mini_shop.db")

engine = create_engine (database_url, connect_args={"check_same_thread" : False })
SessionLocal = sessionmaker( bind= engine, autoflush=False,autocommit = False)

Base=DeclarativeBase()
class Base(DeclarativeBase):
    pass

