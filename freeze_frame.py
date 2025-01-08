import cv2
import numpy as np

class FreezeFrame:
    def __init__(self, video_path, target_frame_rate=30, target_resolution=(1280, 720)):
        self.video_path = video_path
        self.target_frame_rate = target_frame_rate
        self.target_resolution = target_resolution

    def optimize_video(self, output_path):
        # Open the video file
        capture = cv2.VideoCapture(self.video_path)

        # Get original properties
        original_frame_rate = capture.get(cv2.CAP_PROP_FPS)
        original_resolution = (
            int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        output_video = cv2.VideoWriter(output_path, fourcc, self.target_frame_rate, self.target_resolution)

        while capture.isOpened():
            ret, frame = capture.read()
            if not ret:
                break

            # Resize frame
            frame = cv2.resize(frame, self.target_resolution)

            # Write the frame
            output_video.write(frame)

        # Release everything if job is finished
        capture.release()
        output_video.release()

        print(f"Video optimized successfully at {output_path}")

if __name__ == "__main__":
    video_path = "input_video.mp4"
    output_path = "output_video.mp4"
    freeze_frame = FreezeFrame(video_path)
    freeze_frame.optimize_video(output_path)