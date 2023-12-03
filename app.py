# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

from arel import HotReload, Path
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from os import getenv


# --------------------------------------------------------------------------------
# Bootstrap
# --------------------------------------------------------------------------------

load_dotenv()


# --------------------------------------------------------------------------------
# App Creation
# --------------------------------------------------------------------------------

app = FastAPI()


# --------------------------------------------------------------------------------
# Static Files
# --------------------------------------------------------------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")


# --------------------------------------------------------------------------------
# Templates
# --------------------------------------------------------------------------------

templates = Jinja2Templates(directory="template")


# --------------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------------

@app.get("/", summary="Main page that redirects to application", response_class=HTMLResponse)
async def get_index(request:Request):
    return RedirectResponse("/app")


@app.get("/app", summary="Displays the main page", response_class=HTMLResponse)
async def get_generate_password(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})


# --------------------------------------------------------------------------------
# Hot Reload
# --------------------------------------------------------------------------------

if _debug := getenv("DEBUG"):
    hot_reload = HotReload(paths=[Path(".")])
    app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = _debug
    templates.env.globals["hot_reload"] = hot_reload
