# models.py
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Enum,
    Date,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from enum import Enum as PyEnum

from database import Base

class DeviceStatus(PyEnum):
    online = 1
    offline = 0

# Users table
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    contact = Column(String(255), nullable=False)
    name = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

    # Relationship to devices
    devices = relationship("Device", back_populates="user")

# Farms table
class Farm(Base):
    __tablename__ = "farms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    size = Column(Float, nullable=False)

    # Relationship to devices
    devices = relationship("Device", back_populates="farm")

# Towers table
class Tower(Base):
    __tablename__ = "towers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    slots = Column(Integer, nullable=False)

    # Relationship to devices
    devices = relationship("Device", back_populates="tower")

# Devices table
class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tower_id = Column(Integer, ForeignKey("towers.id"), nullable=False)
    farm_id = Column(Integer, ForeignKey("farms.id"), nullable=False)
    status = Column(Enum(DeviceStatus), nullable=False)
    installation_date = Column(Date, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)

    # Relationships
    user = relationship("User", back_populates="devices")
    tower = relationship("Tower", back_populates="devices")
    farm = relationship("Farm", back_populates="devices")