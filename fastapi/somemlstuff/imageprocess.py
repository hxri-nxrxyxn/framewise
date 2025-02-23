import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import joblib
import time

rf_model_loaded = joblib.load("face_pose_model.pkl")

# Initialize MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True)

def calculate_distance(p1, p2):
    """Euclidean distance between two points."""
    return np.linalg.norm(np.array(p1) - np.array(p2))

def calculate_angle(p1, p2, p3):
    """Angle between three points using the cosine rule."""
    a = calculate_distance(p2, p3)
    b = calculate_distance(p1, p3)
    c = calculate_distance(p1, p2)
    if a * b == 0:  # Prevent division by zero
        return 0
    angle = np.arccos((b**2 + c**2 - a**2) / (2 * b * c))
    return np.degrees(angle)

def extract_features_from_image(image_rgb):
    """Extracts face features from an image and returns them as a DataFrame."""
    
    results = face_mesh.process(image_rgb)

    if not results.multi_face_landmarks:
        print("No face detected in the image.")
        return None

    face_landmarks = results.multi_face_landmarks[0]
    landmarks = [(lm.x, lm.y) for lm in face_landmarks.landmark]

    # Required landmark indices
    required_indices = [152, 1, 10, 61, 291, 13, 14]  # Chin, nose, forehead, mouth corners, lips
    if len(landmarks) < max(required_indices):
        print(f"Incomplete landmark data. Only {len(landmarks)} landmarks found.")
        return None

    # Compute features
    features = {
        "chin_to_nose": calculate_distance(landmarks[152], landmarks[1]),  # Chin to nose tip
        "chin_angle": calculate_angle(landmarks[152], landmarks[1], landmarks[10]),  # Chin, nose, forehead
        "mouth_width": calculate_distance(landmarks[61], landmarks[291]),  # Left to right mouth corner
        "mouth_height": calculate_distance(landmarks[13], landmarks[14])  # Upper to lower lip
    }

    # Create DataFrame in the required format
    columns = ["chin_to_nose", "chin_angle", "mouth_width", "mouth_height"]
    return pd.DataFrame([list(features.values())], columns=columns)

cap = cv2.VideoCapture(0)
frame_interval = 1/10  # Capture frame every 2 seconds
last_capture_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    df_new_sample = extract_features_from_image(image_rgb)
    if df_new_sample is not None:
        print(df_new_sample)
        prediction = rf_model_loaded.predict(df_new_sample)
        label = {prediction[0]}

    cv2.putText(frame, f"Pose: {label}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.imshow("Face Feature Extraction", frame)

    # Capture frame every `frame_interval` seconds
    if time.time() - last_capture_time > frame_interval:
        last_capture_time = time.time()

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()


# Example usage:

