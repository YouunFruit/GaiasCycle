from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
app=FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"),name = "static")
@app.get("/", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("home.html",{"request":req})

@app.get("/about", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("about.html",{"request":req})