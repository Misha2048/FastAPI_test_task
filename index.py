from fastapi import FastAPI
from routes.links import link_router

app = FastAPI()

app.include_router(link_router)