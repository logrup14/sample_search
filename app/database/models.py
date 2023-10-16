from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData
Base = declarative_base()


class DocumentBase(Base):
    id = Column(Integer, primary_key=True, index=True)


class Documents(DocumentBase):
    __tablename__ = "documents"
    name = Column(String)
    original_pdf = Column(Text)
    parsed_text = Column(Text)
