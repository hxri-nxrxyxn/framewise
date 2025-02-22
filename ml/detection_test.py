import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp

model = tf.keras.models.load_model("virtual_cameraman_model.h5") #loading the model

CATEGORIES = ["happy", "sad", "neutral", "chin_up", "chin_down", "smile", "no_smile"] #categories used when data was collected

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #face detector(opencv) initialised

mp_pose = mp.solutions.pose #mediapipe model initialisation
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

def preprocess_frame(frame):
    """Preprocess frame for model prediction."""
    frame_resized = cv2.resize(frame, (64, 64))  # frame resize to match model input 
    frame_resized = frame_resized / 255.0  # normalisation factor
    return np.expand_dims(frame_resized, axis=0)  # added dimension

def give_feedback(pred_label):
    """Provide real-time pose and expression adjustment feedback."""
    feedback = {
        "happy": "Great smile! Keep it up.",
        "sad": "Try smiling a bit more!",
        "neutral": "Maintain a confident expression.",
        "chin_up": "Raise your chin slightly for a natural look.",
        "chin_down": "Lower your chin slightly for a better angle.",
        "smile": "Keep that smile!",
        "no_smile": "Try adding a slight smile."
    }
    return feedback.get(pred_label, "")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # face detection

    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]  # face region extraction 
        processed_face = preprocess_frame(face)

        # predictions for emotions according to processed dataset
        predictions = model.predict(processed_face)
        pred_label = CATEGORIES[np.argmax(predictions)]  #max accuracy prediction selected as label

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        feedback_text = give_feedback(pred_label)
        cv2.putText(frame, f"{pred_label}: {feedback_text}", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Virtual Cameraman", frame) #frame display

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
