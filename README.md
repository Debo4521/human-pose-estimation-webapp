# Human Pose Estimation Web App

A real-time human pose estimation web application built using YOLOv8-Pose, FastAPI, Streamlit, and Docker. The application detects human body keypoints, visualizes pose skeletons, and provides downloadable annotated results through an interactive web interface.

## Features

- Human pose estimation using YOLOv8-Pose
- Image upload through a Streamlit web interface
- Real-time keypoint and skeleton visualization
- Multi-person pose detection
- People-count detection
- Downloadable processed images
- FastAPI backend for model inference
- Dockerized deployment
- Modular architecture for image, video, and webcam inference

## Tech Stack

- Python
- PyTorch
- YOLOv8-Pose
- OpenCV
- FastAPI
- Streamlit
- Docker
- Git & GitHub

## Project Structure

```text
human-pose-estimation-webapp/
│
├── app/
│   ├── api.py
│   ├── detector.py
│   ├── test_pose.py
│   ├── video_pose.py
│   └── webcam_pose.py
│
├── frontend/
│   └── streamlit_app.py
│
├── screenshots/
│
├── Dockerfile
├── start.sh
├── requirements.txt
├── .gitignore
├── .dockerignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Debo4521/human-pose-estimation-webapp.git
cd human-pose-estimation-webapp
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

Start the FastAPI backend:

```bash
uvicorn app.api:app --reload
```

Start the Streamlit frontend:

```bash
streamlit run frontend/streamlit_app.py
```

Open:

```text
http://localhost:8501
```

## Run with Docker

Build the Docker image:

```bash
docker build -t pose-estimation-app .
```

Run the container:

```bash
docker run -p 8000:8000 -p 8501:8501 pose-estimation-app
```

Open:

```text
http://localhost:8501
```

## How It Works

1. Upload an image containing one or more people.
2. The image is sent to the FastAPI backend.
3. YOLOv8-Pose performs pose estimation.
4. The application detects body keypoints and skeleton connections.
5. The annotated image is displayed.
6. The processed image can be downloaded.

## Results

The application successfully detects and visualizes human body keypoints using YOLOv8-Pose, supporting multiple people in a single image while providing an easy-to-use web interface.
