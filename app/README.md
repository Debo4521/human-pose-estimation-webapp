# Real-Time Human Pose Estimation Web App

A computer vision application for detecting and visualizing human body keypoints in images using YOLOv8-Pose, FastAPI, and Streamlit.

## Features

- Human pose estimation using YOLOv8-Pose
- Image upload through Streamlit frontend
- FastAPI backend for model inference
- Keypoint and skeleton visualization
- People detection count
- Processed image download
- Supports image, video, and webcam inference scripts

## Tech Stack

- Python
- PyTorch
- YOLOv8-Pose
- OpenCV
- FastAPI
- Streamlit
- Ultralytics

## Project Structure

```text
app/
  api.py
  detector.py
  test_pose.py
  webcam_pose.py
  video_pose.py

frontend/
  streamlit_app.py

samples/
  uploads/
  api_outputs/
  ## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI backend:

```bash
uvicorn app.api:app --reload
```

Start Streamlit frontend:

```bash
streamlit run frontend/streamlit_app.py
```

Open:

```text
http://localhost:8501
```

## Results

The app detects people in uploaded images and generates pose skeleton visualizations with keypoint overlays