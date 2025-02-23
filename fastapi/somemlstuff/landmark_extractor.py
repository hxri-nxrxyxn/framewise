import os
import cv2
import mediapipe as mp
import numpy as np
import pandas as pd


# Define dataset path
dataset_path = "../data"
output_data = []

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True)

# Loop through each folder
for folder_name in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder_name)
    if not os.path.isdir(folder_path):
        continue

    # Loop through images in the folder
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        image = cv2.imread(img_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        results = face_mesh.process(image_rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Extract (x, y) coordinates of landmarks
                landmarks = [(lm.x, lm.y) for lm in face_landmarks.landmark]
                output_data.append({
                    "label": folder_name,
                    "landmarks": landmarks
                })

df = pd.DataFrame(output_data)
df.to_csv("landmarks_data.csv", index=False)

# Print some extracted landmarks
print(output_data[:3])  # See first 3 samples
