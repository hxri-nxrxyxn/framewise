import cv2
import mediapipe as mp
import numpy as np
import csv
import os
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

#MediaPipe Pose for calling later
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

def capture_pose_data(output_csv='pose_data.csv'):
    cap = cv2.VideoCapture(1)
    
    file_exists = os.path.exists(output_csv)
    file = open(output_csv, mode='a', newline='')  
    writer = csv.writer(file)
    
    if not file_exists:  
        writer.writerow([f'kp_{i}' for i in range(33*4)] + ['label'])
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        
        keypoints = []
        if results.pose_landmarks:
            for landmark in results.pose_landmarks.landmark:
                keypoints.extend([landmark.x, landmark.y, landmark.z, landmark.visibility])
            
            label = input("Enter label for current pose: ")
            writer.writerow(keypoints + [label])
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        cv2.imshow('Pose Detection', frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    file.close()  
    cap.release()
    cv2.destroyAllWindows()


def train_model(csv_file='pose_data.csv', model_save_path='pose_model.h5'):
    data = np.loadtxt(csv_file, delimiter=',', skiprows=1)
    X, y = data[:, :-1], data[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = Sequential([
        Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.3),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(32, activation='relu'),
        Dense(len(np.unique(y)), activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))
    model.save(model_save_path)
    print(f'Model saved at {model_save_path}')

if __name__ == "__main__":
    capture_pose_data()
    train_model()
