from ultralytics import YOLO

# Load YOLO pose model
model = YOLO("yolov8s-pose.pt")

def detect_pose(image_path):
    results = model(image_path, save=True)
    return results