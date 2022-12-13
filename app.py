"""Data consumer main app file."""

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import app_routes, management, login

app = FastAPI()
app.include_router(app_routes.router, prefix="/api")
app.include_router(management.router, prefix="/api")
app.include_router(login.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Data Consumer": "Start Page"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=7002, reload=True)
