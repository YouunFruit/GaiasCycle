from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import Depends, HTTPException
from typing import List, Optional
from models import User, Farm, Tower, Device, Slot, DeviceStatus
from database import get_db
from schemas import (
    UserCreate,
    UserRead,
    FarmCreate,
    FarmRead,
    TowerCreate,
    TowerRead,
    DeviceCreate,
    DeviceRead,
    SlotCreate,
    SlotRead,
    DeviceStatusEnum,
)

# USERS CRUD
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)) -> UserRead:
    user = User(
        contact=user_data.contact,
        name=user_data.name,
        username=user_data.username,
        password=user_data.password,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return UserRead.model_validate(user)


async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)) -> UserRead:
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserRead.model_validate(user)


async def get_user_by_username(username: str, db: AsyncSession = Depends(get_db)) -> UserRead:
    stmt = select(User).where(User.username == username)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserRead.model_validate(user)


# FARMS CRUD
async def create_farm(farm_data: FarmCreate, db: AsyncSession = Depends(get_db)) -> FarmRead:
    farm = Farm(lat=farm_data.lat, lon=farm_data.lon, size=farm_data.size)
    db.add(farm)
    await db.commit()
    await db.refresh(farm)
    return FarmRead.model_validate(farm)


async def get_farm_by_id(farm_id: int, db: AsyncSession = Depends(get_db)) -> FarmRead:
    stmt = select(Farm).where(Farm.id == farm_id)
    result = await db.execute(stmt)
    farm = result.scalar_one_or_none()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return FarmRead.model_validate(farm)

async def get_farms( db: AsyncSession = Depends(get_db)) -> FarmRead:
    stmt = select(Farm)
    result = await db.execute(stmt)
    farm = result.scalar()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return FarmRead.model_validate(farm)


# TOWERS CRUD
async def create_tower(tower_data: TowerCreate, db: AsyncSession = Depends(get_db)) -> TowerRead:
    tower = Tower(
        farm_id=tower_data.farm_id,
        slot_amount=tower_data.slot_amount,
    )
    db.add(tower)
    await db.commit()
    await db.refresh(tower)
    return TowerRead.model_validate(tower)

async def get_towers( db: AsyncSession = Depends(get_db)) -> TowerRead:
    stmt = select(Tower)
    result = await db.execute(stmt)
    tower = result.scalar()
    if not tower:
        raise HTTPException(status_code=404, detail="Tower not found")
    return TowerRead.model_validate(tower)

async def get_devices( db: AsyncSession = Depends(get_db)) -> DeviceRead:
    stmt = select(Device)
    result = await db.execute(stmt)
    device = result.scalar()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return DeviceRead.model_validate(device)

async def get_slots( db: AsyncSession = Depends(get_db)) -> SlotRead:
    stmt = select(Slot)
    result = await db.execute(stmt)
    slot = result.scalar()
    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found")
    return SlotRead.model_validate(slot)

async def get_tower_by_id(tower_id: int, db: AsyncSession = Depends(get_db)) -> TowerRead:
    stmt = select(Tower).where(Tower.id == tower_id)
    result = await db.execute(stmt)
    tower = result.scalar_one_or_none()
    if not tower:
        raise HTTPException(status_code=404, detail="Tower not found")
    return TowerRead.model_validate(tower)


# DEVICES CRUD
async def create_device(device_data: DeviceCreate, db: AsyncSession = Depends(get_db)) -> DeviceRead:
    device = Device(
        farm_id=device_data.farm_id,
        tower_id=device_data.tower_id,
        slot_id=device_data.slot_id,
        device_type=device_data.device_type,
        value=device_data.value,
        unit=device_data.unit,
        status=DeviceStatus[device_data.status.upper()],
    )
    db.add(device)
    await db.commit()
    await db.refresh(device)
    return DeviceRead.model_validate(device)


async def get_device_by_id(device_id: int, db: AsyncSession = Depends(get_db)) -> DeviceRead:
    stmt = select(Device).where(Device.id == device_id)
    result = await db.execute(stmt)
    device = result.scalar_one_or_none()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return DeviceRead.model_validate(device)


async def get_devices_by_user_id(user_id: int, db: AsyncSession = Depends(get_db)) -> List[DeviceRead]:
    stmt = select(Device).where(Device.user_id == user_id)
    result = await db.execute(stmt)
    devices = result.scalars().all()
    return [DeviceRead.model_validate(device) for device in devices]


# SLOTS CRUD
async def create_slot(slot_data: SlotCreate, db: AsyncSession = Depends(get_db)) -> SlotRead:
    slot = Slot(
        tower_id=slot_data.tower_id,
        crop=slot_data.crop,
        planted_date=slot_data.date_filled,
        expected_harvest=slot_data.expected_harvest,
    )
    db.add(slot)
    await db.commit()
    await db.refresh(slot)
    return SlotRead.model_validate(slot)


async def get_slot_by_id(slot_id: int, db: AsyncSession = Depends(get_db)) -> SlotRead:
    stmt = select(Slot).where(Slot.id == slot_id)
    result = await db.execute(stmt)
    slot = result.scalar_one_or_none()
    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found")
    return SlotRead.model_validate(slot)
