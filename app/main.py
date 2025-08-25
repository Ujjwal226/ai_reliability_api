from fastapi import FastAPI
from app.routers import health
from app.core.config import APP_NAME, API_VERSION


app = FastAPI(
    title=APP_NAME,
    description="APIs for serving models, monitoring, and system status",
    version=API_VERSION
)


app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Welcome to the AI Reliability Dashboard API"}

if __name__ == "__main__":
    import asyncio
    import sys
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    from fastapi.routing import APIRouter
    import uvicorn  

    print("Starting FastAPI server...")

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
