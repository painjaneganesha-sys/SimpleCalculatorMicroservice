from fastapi import FastAPI

from handlers.calculatehandler import calculaterouter
from handlers.healthcheckhandler import healthrouter


def get_app():

    app = FastAPI(
        title="Simple Calculator Microservice"
    )

    app.include_router(calculaterouter)
    app.include_router(healthrouter)

    return app