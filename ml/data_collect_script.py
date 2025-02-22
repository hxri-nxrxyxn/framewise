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
    cap = cv2.VideoCapture(0)
    data = []    
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
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
    
    cap.release()
    cv2.destroyAllWindows()