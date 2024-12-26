from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
from enum import Enum

# Enum for Device Status
class DeviceStatusEnum(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"

class DeviceTypeEnum(str, Enum):
    FARM = "farm"
    TOWER = "tower"
    SLOT = "slot"

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
    tower_id: int
    farm_id: int
    slot_id: int
    device_type: DeviceTypeEnum
    status: DeviceStatusEnum
    value: int
    unit: str


class DeviceCreate(DeviceBase):
    pass

class DeviceRead(DeviceBase):
    id: int

    class Config:
        from_attributes = True

class SlotBase(BaseModel):
    tower_id:int
    crop: str
    date_filled: str
    expected_harvest:str

class SlotCreate(SlotBase):
    pass

class SlotRead(SlotBase):
    id: int

    class Config:
        from_attributes = True