import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True)

image_path = "../data/chin_down/10.jpg"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = face_mesh.process(image_rgb)

if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        for idx, landmark in enumerate(face_landmarks.landmark):
            h, w, _ = image.shape
            x, y = int(landmark.x * w), int(landmark.y * h)
            cv2.circle(image, (x, y), 1, (0, 255, 0), -1)

cv2.imshow("Face Landmarks", image)
cv2.waitKey(0)
cv2.destroyAllWindows()