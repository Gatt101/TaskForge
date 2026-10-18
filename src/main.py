from fastapi import FastAPI
from src.modules.jobs.router import router as jobs_router

app = FastAPI(
title="My FastAPI Application",
description="A simple FastAPI application",
version="0.1.0"
)

app.include_router(jobs_router)

@app.get("/home")
def root():
    return {"message": "Hello, World!"}