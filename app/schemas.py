from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
from enum import Enum

# Enum for Device Status
class DeviceStatusEnum(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"

# User Schema
class UserBase(BaseModel):
    contact: str
    name: str
    username: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True

# Farm Schema
class FarmBase(BaseModel):
    lat: float
    lon: float
    size: float

class FarmCreate(FarmBase):
    pass

class FarmRead(FarmBase):
    id: int

    class Config:
        from_attributes = True

# Tower Schema
class TowerBase(BaseModel):
    tower_id: str
    lat: float
    lon: float
    slots: int

class TowerCreate(TowerBase):
    pass

class TowerRead(TowerBase):
    id: int

    class Config:
        from_attributes = True

# Device Schema
class DeviceBase(BaseModel):
    user_id: int
    tower_id: int
    farm_id: int
    status: DeviceStatusEnum
    installation_date: date
    lat: float
    lon: float

class DeviceCreate(DeviceBase):
    pass

class DeviceRead(DeviceBase):
    id: int

    class Config:
        from_attributes = True
