# models.py
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):  # Existing User model
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    contact = Column(String(100), unique=True, index=True)
    type = Column(Enum)
    hashed_password = Column(String(255))
    gardens = relationship("Garden", back_populates="owner")