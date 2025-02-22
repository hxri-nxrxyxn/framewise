from fastapi import FastAPI, WebSocket
import base64
from io import BytesIO
from PIL import Image
import cv2
import numpy as np
import asyncio

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
            print("Waiting for Frame")
            start_time = asyncio.get_event_loop().time()
            data = await websocket.receive_text()  # Receive Base64 string
            frame_data = data.replace('data:image/jpeg;base64,', '')  # Remove header
            frame_bytes = base64.b64decode(frame_data)  # Decode Base64
            nparr = np.frombuffer(frame_bytes, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            cv2.imshow("stuff", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            elapsed_time = asyncio.get_event_loop().time() - start_time
            sleep_time = max(0, FRAME_DELAY - elapsed_time)
            await asyncio.sleep(sleep_time)

            print("Frame Received and Displayed")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()
