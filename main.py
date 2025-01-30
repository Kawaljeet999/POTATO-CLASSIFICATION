from fastapi import FastAPI, File, UploadFile
from tensorflow import keras
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Request

app = FastAPI()

# Serve static files (like styles.css)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="templates")

MODEL = tf.keras.models.load_model("./saved_models/1.keras")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# @app.get("/ping")
# async def ping():  # Check if the server is alive or not
#     return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):  # Render the home page (index.html)
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())  # Read the entire file content as bytes
    img_batch = np.expand_dims(image, 0)  # Increment dimension
    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }
