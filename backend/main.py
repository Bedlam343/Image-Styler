from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

from io import BytesIO
import numpy as np
from PIL import Image
import cv2

from sketch import noodlefy, pencil_sketch, cartoonize, water_sketch, find_contours

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

@app.post("/image/noodlefy")
async def convert_image(file: UploadFile):
    if file is not None:
        try:
            contents = await file.read()
            image = Image.open(BytesIO(contents))
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid image file")
        
        image_sketch = noodlefy(np.array(image))
        im_pil = Image.fromarray(image_sketch)

        buf = BytesIO()
        im_pil.save(buf, format="PNG")
        buf.seek(0)

        return Response(content=buf.read(), media_type="image/png")

    raise HTTPException(
        status_code=400,
        detail="No image was sent."
    )
