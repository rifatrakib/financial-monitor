from fastapi import FastAPI

from . import config

app = FastAPI()


@app.get("/")
def index():
    app_name = config.read_config("app_name")
    return {"message": f"Welcome to {app_name}"}
