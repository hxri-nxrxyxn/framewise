from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio

app = FastAPI()

@app.get("/")
def get():
    return "Hello World"