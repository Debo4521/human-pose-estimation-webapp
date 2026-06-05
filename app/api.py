from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from ultralytics import YOLO
import shutil
import os
import cv2

app = FastAPI(title="Real-Time Pose Estimation API")

model = YOLO("yolov8s-pose.pt")

UPLOAD_DIR = "samples/uploads"
OUTPUT_DIR = "samples/api_outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

latest_output_path = os.path.join(OUTPUT_DIR, "latest_output.jpg")


@app.get("/")
def home():
    return {"message": "Pose Estimation API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict/image")
async def predict_image(file: UploadFile = File(...)):
    input_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = model(input_path)

    people_detected = len(results[0].keypoints)

    annotated_image = results[0].plot()

    cv2.imwrite(latest_output_path, annotated_image)

    return JSONResponse({
        "filename": file.filename,
        "people_detected": people_detected,
        "output_image_path": latest_output_path,
        "message": "Pose detection completed successfully"
    })


@app.get("/output/latest")
def get_latest_output():
    if not os.path.exists(latest_output_path):
        return JSONResponse(
            {"error": "No output image found"},
            status_code=404
        )

    return FileResponse(latest_output_path, media_type="image/jpeg")