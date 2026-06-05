import cv2
from ultralytics import YOLO

model = YOLO("yolov8s-pose.pt")

video_path = "samples/input_video.mp4"

cap = cv2.VideoCapture(video_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter(
    "samples/output_video.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    out.write(annotated_frame)

    cv2.imshow("Pose Estimation", annotated_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q") or key == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video processing completed!")