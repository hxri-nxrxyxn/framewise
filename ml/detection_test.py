import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp

# Load the trained emotion model
model = tf.keras.models.load_model("virtual_cameraman_model.h5")

# Categories used during training
CATEGORIES = ["happy", "sad", "neutral", "chin_up", "chin_down", "smile"]

# Define score mapping for emotions
emotion_scores = {
    "happy": 65,
    "sad": 15,
    "neutral": 15,
    "chin_up": 15,
    "chin_down": 15,
    "smile": 25
}

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

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
        "smile": "Smile some more!"
    }
    return feedback.get(pred_label, "")

def analyze_posture(landmarks, frame):
    """Analyze body posture and provide feedback and score based on shoulder alignment."""
    height, width, _ = frame.shape

    left_shoulder = (int(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].x * width),
                     int(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y * height))
    right_shoulder = (int(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width),
                      int(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height))

    head_tilt = left_shoulder[1] - right_shoulder[1]  

    if abs(head_tilt) > 20:
        return "Good! Maintain that pose!", 50
    else:
        return "Loosen up!", 25

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

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_results = face_detection.process(frame_rgb)
        emotion_text = ""
        emotion_score = 0

        if face_results.detections:
            detection = face_results.detections[0]
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

            face_img = frame[y:y + box_height, x:x + box_width]
            if face_img.size > 0 and box_width >= 20 and box_height >= 20:
                processed_face = preprocess_frame(face_img)
                predictions = model.predict(processed_face)
                pred_label = CATEGORIES[np.argmax(predictions)]
                emotion_score = emotion_scores.get(pred_label, 0)
                feedback_text = give_feedback(pred_label)

                cv2.rectangle(frame, (x, y), (x + box_width, y + box_height), (255, 0, 0), 2)
                cv2.putText(frame, f"{pred_label} ({emotion_score}): {feedback_text}", (x, y - 10),
                            cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 2)

        pose_results = pose.process(frame_rgb)
        posture_text = ""
        posture_score = 0
        if pose_results.pose_landmarks:
            posture_text, posture_score = analyze_posture(pose_results.pose_landmarks.landmark, frame)
            cv2.putText(frame, f"Posture: {posture_text} ({posture_score})", (50, 50),
                        cv2.FONT_HERSHEY_TRIPLEX, 0.7, (0, 0, 255), 2)
            #mp.solutions.drawing_utils.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS) #optional, to draw landmarks
            # Total Score Calculation
            
        score = emotion_score + posture_score
        cv2.putText(frame, f"Total Score: {score}", (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        cv2.imshow("Virtual Cameraman", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
