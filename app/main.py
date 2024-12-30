from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

from crud import *
from database import engine, Base

app=FastAPI()

@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"),name = "static")
@app.get("/", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("home.html",{"request":req})

@app.get("/about", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("aboutUs.html",{"request":req})

@app.get("/maps", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("maps.html",{"request":req})

@app.get("/contactUs", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("contactUs.html",{"request":req})
@app.get("/admin/IOT", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("IOT.html",{"request":req})

@app.get("/admin/addDevice", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("addDevice.html",{"request":req})

@app.get("/admin/addFarm", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("addFarm.html",{"request":req})

@app.get("/admin/addUser", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("addUser.html",{"request":req})

@app.get("/admin/listDevices", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("listDevices.html",{"request":req})

@app.get("/admin/listFarms", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("listFarms.html",{"request":req})

@app.get("/admin/statistics", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("statistics.html",{"request":req})

@app.get("/admin/listInventory", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("listInventory.html",{"request":req})

# @app.get("/signUp", response_class=HTMLResponse)
# async def read_root(req:Request):
#     return templates.TemplateResponse("signUp.html",{"request":req})

@app.get("/tutorial", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("tutorial.html",{"request":req})

@app.get("/admin/updates", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("updates.html",{"request":req})

@app.get("/admin/listUsers", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("listUsers.html",{"request":req})

# @app.get("/login", response_class=HTMLResponse)
# async def read_root(req:Request):
#     return templates.TemplateResponse("logIn.html",{"request":req})

@app.get("/admin", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("dashboard.html",{"request":req})

@app.get("/admin/stats", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("stats.html",{"request":req})

@app.get("/admin/addCrop", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("addCrop.html",{"request":req})



@app.get("/admin/listTowers", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("listTowers.html",{"request":req})

@app.get("/admin/listCrops", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("listCrops.html",{"request":req})

@app.get("/admin/addTower", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("addTower.html",{"request":req})

# USER ENDPOINTS
@app.post("/api/user", response_model=UserRead)
async def api_create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(user, db)


@app.get("/api/user/{user_id}", response_model=UserRead)
async def api_get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    return await get_user_by_id(user_id, db)


@app.get("/api/user/username/{username}", response_model=UserRead)
async def api_get_user_by_username(username: str, db: AsyncSession = Depends(get_db)):
    return await get_user_by_username(username, db)


# FARM ENDPOINTS
@app.post("/api/farm", response_model=FarmRead)
async def api_create_farm(farm: FarmCreate, db: AsyncSession = Depends(get_db)):
    return await create_farm(farm, db)

@app.get("/api/farm", response_model=FarmRead)
async def api_get_farms( db: AsyncSession = Depends(get_db)):
    return await get_farms(db)


@app.get("/api/farm/{farm_id}", response_model=FarmRead)
async def api_get_farm_by_id(farm_id: int, db: AsyncSession = Depends(get_db)):
    return await get_farm_by_id(farm_id, db)


# TOWER ENDPOINTS
@app.post("/api/tower", response_model=TowerRead)
async def api_create_tower(tower: TowerCreate, db: AsyncSession = Depends(get_db)):
    return await create_tower(tower, db)

@app.get("/api/tower", response_model=FarmRead)
async def api_get_towers( db: AsyncSession = Depends(get_db)):
    return await get_towers(db)


@app.get("/api/tower/{tower_id}", response_model=TowerRead)
async def api_get_tower_by_id(tower_id: int, db: AsyncSession = Depends(get_db)):
    return await get_tower_by_id(tower_id, db)


# DEVICE ENDPOINTS
@app.post("/api/device", response_model=DeviceRead)
async def api_create_device(device: DeviceCreate, db: AsyncSession = Depends(get_db)):
    return await create_device(device, db)

@app.get("/api/device", response_model=List[DeviceRead])
async def api_get_devices(db: AsyncSession = Depends(get_db)):
    return await get_devices(db)

@app.get("/api/device/{device_id}", response_model=DeviceRead)
async def api_get_device_by_id(device_id: int, db: AsyncSession = Depends(get_db)):
    return await get_device_by_id(device_id, db)

@app.get("/api/device/user/{user_id}", response_model=List[DeviceRead])
async def api_get_devices_by_user_id(user_id: int, db: AsyncSession = Depends(get_db)):
    return await get_devices_by_user_id(user_id, db)

# SLOT ENDPOINTS
@app.post("/api/slot", response_model=SlotRead)
async def api_create_slot(slot: SlotCreate, db: AsyncSession = Depends(get_db)):
    return await create_slot(slot, db)

@app.get("/api/slot", response_model=List[SlotRead])
async def api_get_slots(db: AsyncSession = Depends(get_db)):
    return await get_slots(db)

@app.get("/api/slot/{slot_id}", response_model=SlotRead)
async def api_get_slot_by_id(slot_id: int, db: AsyncSession = Depends(get_db)):
    return await get_slot_by_id(slot_id, db)
