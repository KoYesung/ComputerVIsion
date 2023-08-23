import cv2
import os

def video_to_frames(video_path, output_folder, duration=20):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frames_to_capture = int(fps * duration)
    os.makedirs(output_folder, exist_ok=True)

    frame_count = 0

    while cap.isOpened() and frame_count < frames_to_capture:
        ret, frame = cap.read()
        if not ret:
            break

        frame_filename = f"frame_{frame_count:04d}.jpg"
        frame_path = os.path.join(output_folder, frame_filename)
        cv2.imwrite(frame_path, frame)

        frame_count += 1

    cap.release()

if __name__ == "__main__":
    video_path = "Mudo.mp4"
    output_folder = "./img_frames"
    duration = 20
    video_to_frames(video_path, output_folder)
    print("Frames extracted and saved successfully.")