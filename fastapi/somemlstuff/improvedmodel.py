import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image

class_names = ["chin_down", "chin_up", "happy", "neutral", "sad", "smile"]
model = models.load_model("face_mesh_classifier.h5")
# Define constants
IMG_SIZE = (128, 128)  # Resize images

def predict_image(img):
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Expand dimensions

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    
    return predicted_class

# Initialize Face Mesh model
mp_face_mesh = mp.solutions.face_mesh
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)
model = tf.keras.models.load_model("face_mesh_classifier.h5")
print("Model loaded successfully!")

class_names = ["chin_down", "chin_up", "happy", "neutral", "sad", "smile"] 

# Initialize webcam
cap = cv2.VideoCapture(0)  # Change to 1 if using an external camera

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB (MediaPipe requirement)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces using OpenCV
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    for (x, y, w, h) in faces:
        # Draw face bounding box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract face ROI and process with MediaPipe
        face_roi = frame[y:y+h, x:x+w]
        face_resized = cv2.resize(face_roi, (128, 128))
        face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(face_rgb)

        # Create a black screen for drawing the mesh
        mesh_image = np.zeros_like(face_rgb)

        if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    mesh_image = np.zeros_like(frame)
                    for lm in face_landmarks.landmark:  
                        lm_x = int(x + lm.x * w)
                        lm_y = int(y + lm.y * h)

                        cv2.circle(mesh_image, (lm_x, lm_y), 1, (255, 255, 255), -1)
                mesh_image = mesh_image[y:y+h, x:x+w]
                mesh_image = cv2.resize(mesh_image, (128, 128))

        predicted_class = predict_image(mesh_image)

        # Display predicted class
        cv2.putText(frame, predicted_class, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)


        cv2.imshow("Face Mesh", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
