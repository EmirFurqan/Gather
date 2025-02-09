from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL= 'postgresql+asyncpg://postgres:0@localhost:5432/gather'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
