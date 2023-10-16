import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

# Database connection settings using environment variables
DATABASE_USER = os.getenv("POSTGRES_USER")
DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_HOST = os.getenv("POSTGRES_HOST")
DATABASE_PORT = os.getenv("POSTGRES_PORT")
DATABASE_NAME = os.getenv("POSTGRES_DB")

# Construct the DATABASE_URL using environment variables
DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a Session class for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Function to create the database if it does not exist
def create_database_if_not_exists():
    inspector = inspect(engine)
    if not inspector.has_database(DATABASE_NAME):
        engine.execute(f"CREATE DATABASE {DATABASE_NAME}")


# Call the function to create the database if it does not exist
create_database_if_not_exists()
