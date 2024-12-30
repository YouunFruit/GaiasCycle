from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, date
from enum import Enum

from pydantic.v1 import validator


# Enum for Device Status
class DeviceStatusEnum(str, Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"

class DeviceTypeEnum(str, Enum):
    FARM = "FARM"
    TOWER = "TOWER"
    SLOT = "SLOT"

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
    farm_id: int
    slot_amount: int

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
    installation_date: date

    class Config:
        use_enum_values = True

class DeviceCreate(DeviceBase):
    pass

class DeviceRead(DeviceBase):
    id: int

    class Config:
        from_attributes = True

class SlotBase(BaseModel):
    tower_id:int
    crop: str
    date_filled: date
    expected_harvest: date

class SlotCreate(SlotBase):
    @validator("planted_date", "expected_harvest", "date_filled", pre=True)
    def validate_dates(cls, value):
        if isinstance(value, date):  # Already a date object
            return value
        try:
            # Convert string formats to `date` object
            return datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            try:
                return datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Invalid date format. Use DD/MM/YYYY or YYYY-MM-DD.")
    pass

class SlotRead(SlotBase):
    id: int

    class Config:
        from_attributes = True