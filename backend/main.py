from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from io import BytesIO
import numpy as np
from PIL import Image
import cv2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/image")
async def convert_image(image: UploadFile = File(...)):
    contents = await image.read()
    print(contents)