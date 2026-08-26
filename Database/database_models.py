from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Patient_Database(Base):
    __tablename__ = "patients_database"

    id = Column(String,primary_key=True,nullable=False)
    name = Column(String,index=True,nullable=False)
    age = Column(Integer,nullable=False)
    gender = Column(String,nullable=False)
    height = Column(Integer,nullable=False)
    weight = Column(Integer,nullable=False)
    problem = Column(String,nullable=False)
    email = Column(String)
    phone_no = Column(String,nullable=False)
    emergency_phone_no = Column(String)