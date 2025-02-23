from fastapi import FastAPI, WebSocket
import base64
from io import BytesIO
from PIL import Image
import cv2
import numpy as np
import asyncio
from script import run

app = FastAPI()

FRAME_DELAY = 5 / 100

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket Connected")

    try:
        while True:
            start_time = asyncio.get_event_loop().time()
            data = await websocket.receive_text()  # Receive Base64 string
            frame_data = data.replace('data:image/jpeg;base64,', '')  # Remove header
            if not frame_data:
                continue
            await run(frame_data,websocket)


    except Exception as e:
        print(e)
    finally:
        await websocket.close()
