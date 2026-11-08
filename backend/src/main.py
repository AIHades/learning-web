import uvicorn
import sys
import os

from fastapi import FastAPI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.routers.homepage import router as router_homepage
from api.routers.about_us import router as router_about_us
from api.routers.contact import router as router_contact
from api.routers.properties import router as router_properties
from api.routers.services import router as router_services


app = FastAPI()
app.include_router(router_homepage)
app.include_router(router_about_us)
app.include_router(router_contact)
app.include_router(router_properties)
app.include_router(router_services)

if __name__ == "__main__":
    uvicorn.run("main:app" ,reload=True)