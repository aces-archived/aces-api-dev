import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core import config
from db.mongo import connect, close, get_collection
from api.v1.router import router

app = FastAPI(title=config.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect)
app.add_event_handler("shutdown", close)


'''
import random
import string
from typing import List


daftar: List[str] = []

'''
# @app.get("/", summary="Test API")
# async def test_api():
#     return {"test": "API"}

app.include_router(router, prefix="/v1")
