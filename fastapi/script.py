import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp
import base64   

model = tf.keras.models.load_model("virtual_cameraman_model.h5")

CATEGORIES = ["chin_down", "chin_up", "happy", "neutral", "sad", "smile"]

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

REFERENCE_POSE = {
    'LEFT_WRIST': [0.3, 0.8],  # left arm raised
    'RIGHT_WRIST': [0.7, 0.8]   # hopefully right arm raised
}
def decode_base64_frame(encoded_str):
    """Decodes a base64 image string into an OpenCV frame."""
    img_data = base64.b64decode(encoded_str)
    np_arr = np.frombuffer(img_data, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

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

def simple_pose_similarity(landmarks):
    """Dummy similarity calculation using wrist positions"""
    similarity = 0
    if landmarks:
        lw = mp_pose.PoseLandmark.LEFT_WRIST.value
        rw = mp_pose.PoseLandmark.RIGHT_WRIST.value
        
        left_wrist = [landmarks[lw].x, landmarks[lw].y]
        right_wrist = [landmarks[rw].x, landmarks[rw].y]

        # Simple distance comparison
        left_diff = np.linalg.norm(np.array(left_wrist) - np.array(REFERENCE_POSE['LEFT_WRIST']))
        right_diff = np.linalg.norm(np.array(right_wrist) - np.array(REFERENCE_POSE['RIGHT_WRIST']))
        
        # Convert to similarity percentage (0-100)
        similarity = 100 - ((left_diff + right_diff) * 50)
        similarity = np.clip(similarity, 0, 100)
    
    return similarity

async def run(base64,websocket):
    
    frame = decode_base64_frame(base64)
    if frame is None:
        print("No frame captured")
        return
    h, w = frame.shape[:2]
    
    # Handle key presses
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()
    selected_pose = True
    print("Demo pose comparison activated")

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # detection and emotion scoring
    emotion_score = 0
    face_results = face_detection.process(frame_rgb)
    if face_results.detections:
        detection = face_results.detections[0]
        bboxC = detection.location_data.relative_bounding_box
        x = int(bboxC.xmin * w)
        y = int(bboxC.ymin * h)
        box_width = int(bboxC.width * w)
        box_height = int(bboxC.height * h)

        x = max(0, x)
        y = max(0, y)
        box_width = min(box_width, w - x)
        box_height = min(box_height, h - y)

        face_img = frame[y:y + box_height, x:x + box_width]
        if face_img.size > 0 and box_width >= 20 and box_height >= 20:
            processed_face = preprocess_frame(face_img)
            predictions = model.predict(processed_face)
            pred_label = CATEGORIES[np.argmax(predictions)]
            emotion_score = emotion_scores.get(pred_label, 0)
            feedback_text = give_feedback(pred_label)

            cv2.rectangle(frame, (x, y), (x + box_width, y + box_height), (255, 0, 0), 2)
            cv2.putText(frame, f"{pred_label} ({emotion_score}): {feedback_text}", 
                        (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 2)

    # analysis and demo comparison
    posture_score = 0
    similarity = 0
    pose_results = pose.process(frame_rgb)
    if pose_results.pose_landmarks:
        # analysis part for posture?
        posture_text, posture_score = analyze_posture(pose_results.pose_landmarks.landmark, frame)
        cv2.putText(frame, f"Posture: {posture_text} ({posture_score})", 
                    (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (0, 0, 255), 2)

        if selected_pose:
            similarity = simple_pose_similarity(pose_results.pose_landmarks.landmark)
            cv2.putText(frame, f"Demo Pose Match: {int(similarity)}%", 
                        (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            
            # reference pose markers being drawn
            
            for point in REFERENCE_POSE.values():
                cv2.circle(frame, (int(point[0]*w), int(point[1]*h)), 
                            10, (0, 0, 255), -1)

    # Total Score Calculation  
    score = emotion_score + posture_score
    cv2.putText(frame, f"Total Score: {score}", (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
    
    cv2.imshow("Virtual Cameraman", frame)
    await websocket.send_text(str(score)+","+str(similarity)+","+str(emotion_score)+","+str(posture_score)+","+str(feedback_text)+","+str(pred_label)+","+str(selected_pose)) 

cv2.destroyAllWindows()