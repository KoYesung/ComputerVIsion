import cv2
import torch
import torchvision
import seaborn

video_path = 'test_mudo.mp4'
model_path = 'best.pt'  # Path to your YOLOv5 model weights

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5:v5.0', 'yolov5s', pretrained=False)
model.load_state_dict(torch.load(model_path)['model'].state_dict())
model.eval()

# Open the video file
cap = cv2.VideoCapture(video_path)

start_time = None
end_time = 10  # 10초만 테스트

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if start_time is None:
        start_time = cv2.getTickCount() / cv2.getTickFrequency()

    current_time = cv2.getTickCount() / cv2.getTickFrequency()
    elapsed_time = current_time - start_time

    if elapsed_time > end_time:
        break

    results = model(frame)

    frame_with_detections = results.render()[0]

    cv2.imshow('YOLOv5 Object Detection', frame_with_detections)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
