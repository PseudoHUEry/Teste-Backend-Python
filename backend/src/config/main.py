from fastapi import FastAPI
from dotenv import dotenv_values
import os

config = {**os.environ, **dotenv_values(".env")}
app = FastAPI()

def get_config():
    return config

def get_app():
    return app

