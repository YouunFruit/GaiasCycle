from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

from app.database import engine, Base

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
