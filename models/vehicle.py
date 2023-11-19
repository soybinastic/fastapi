from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, BigInteger, DateTime, Text
from sqlalchemy import ForeignKey
from sqlalchemy import Identity
from sqlalchemy.orm import relationship
Base = declarative_base()


class Vehicle(Base):
    __tablename__ = 'vehicle_vehicle'

    id = Column(BigInteger, Identity(start=1, increment=1, minvalue=1,
                maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    vin = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)