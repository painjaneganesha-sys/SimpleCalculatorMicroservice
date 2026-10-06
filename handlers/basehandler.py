from fastapi import FastAPI

from handlers.calculatehandler import calculaterouter
from handlers.healthcheckhandler import healthrouter

all_routers = [calculaterouter,healthrouter]

def get_app():
    app = FastAPI(title="Simple Calculator Microservice")
    for router in all_routers :
        app.include_router(router)
    return app