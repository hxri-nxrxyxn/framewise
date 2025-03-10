import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import mediapipe as mp

dataset_path = "../data_augmented"  # Folder with images
output_path = "../data_mesh"  # Folder to save processed images
os.makedirs(output_path, exist_ok=True)

# Paths
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
dataset_path = "../data_augmented"  # Path to augmented dataset
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)

# Load images and labels
images, labels = [], []

for folder_name in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder_name)
    save_folder = os.path.join(output_path, folder_name)
    os.makedirs(save_folder, exist_ok=True)

    if not os.path.isdir(folder_path):
        continue

    # Process each image
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        frame = cv2.imread(img_path)
        if frame is None:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_roi = frame[y:y+h, x:x+w]
            face_resized = cv2.resize(face_roi, (256, 256))
            face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)

            results = face_mesh.process(face_rgb)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    mesh_image = np.zeros_like(frame)
                    for lm in face_landmarks.landmark:  
                        lm_x = int(x + lm.x * w)
                        lm_y = int(y + lm.y * h)

                        cv2.circle(mesh_image, (lm_x, lm_y), 1, (255, 255, 255), -1)
                save_path = os.path.join(save_folder, img_name)
                mesh_image = mesh_image[y:y+h, x:x+w]
                mesh_image = cv2.resize(mesh_image, (128, 128))
                cv2.imwrite(save_path, mesh_image)

print("✅ Facial meshes extracted and saved!")
