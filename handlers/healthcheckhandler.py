from fastapi import APIRouter

healthrouter = APIRouter(prefix="/health")


@healthrouter.get("/")
async def get_health():
    version = "0.0.0.001"
    return {"status": "UP", "message": ("Simple Calculator Microservice " f"Is Up & Running Version: {version}"),"version": version}