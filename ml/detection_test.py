import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp

# Load the trained emotion model
model = tf.keras.models.load_model("virtual_cameraman_model.h5")

# Categories used during training
CATEGORIES = ["happy", "sad", "neutral", "chin_up", "chin_down", "smile"]

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

def preprocess_frame(face_img):
    """Resize and normalize the face image for model prediction."""
    face_resized = cv2.resize(face_img, (64, 64))
    face_normalized = face_resized / 255.0
    return np.expand_dims(face_normalized, axis=0)

def give_feedback(pred_label):
    """Return feedback based on the predicted emotion label."""
    feedback = {
        "happy": "Great smile! Keep it up.",
        "sad": "Try smiling a bit more!",
        "neutral": "Maintain a confident expression.",
        "chin_up": "Lower your chin slightly for a better angle.",
        "chin_down": "Raise your chin slightly for a natural look.",
        "smile": "Smile some more!",
    }
    return feedback.get(pred_label, "")

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Convert frame to RGB for MediaPipe processing
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)

        # If faces are detected
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x = int(bboxC.xmin * w)
                y = int(bboxC.ymin * h)
                box_width = int(bboxC.width * w)
                box_height = int(bboxC.height * h)

                x = max(0, x)
                y = max(0, y)
                if x + box_width > w:
                    box_width = w - x
                if y + box_height > h:
                    box_height = h - y

                # Extract the face region for processing
                face_img = frame[y:y + box_height, x:x + box_width]
                # Skip frame if the detected face is too small
                if face_img.size == 0 or box_width < 20 or box_height < 20:
                    continue

                processed_face = preprocess_frame(face_img)
                predictions = model.predict(processed_face)
                pred_label = CATEGORIES[np.argmax(predictions)]
                feedback_text = give_feedback(pred_label)

                # Draw bounding box and feedback on the original frame
                cv2.rectangle(frame, (x, y), (x + box_width, y + box_height), (255, 0, 0), 2)
                cv2.putText(frame, f"{pred_label}: {feedback_text}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Virtual Cameraman", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
