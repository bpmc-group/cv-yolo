import cv2
from ultralytics import YOLO

# Load the YOLOv11 model
model = YOLO('resources/model/yolo11s-seg.pt')

# Open the video file
video_path = "resources/video/fall5.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv11 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLO Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # break the loop when the end of the video is reached
        break

cap.release()
cv2.destroyAllWindows()
