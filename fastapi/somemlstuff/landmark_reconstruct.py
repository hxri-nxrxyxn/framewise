import pandas as pd
import ast
import numpy as np

# Load CSV
df = pd.read_csv("landmarks_data.csv")

df["landmarks"] = df["landmarks"].apply(ast.literal_eval)

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

def extract_features(landmarks):
    """Extract useful features from facial landmarks."""
    features = {}

    # Ensure landmarks list has enough points
    required_indices = [152, 1, 10, 61, 291, 13, 14]  # Chin, nose, forehead, mouth corners, lips
    if len(landmarks) < max(required_indices):
        print(f"Skipping entry, only {len(landmarks)} landmarks found.")
        return None  # Skip this row if landmarks are incomplete

    # Compute features safely
    features["chin_to_nose"] = calculate_distance(landmarks[152], landmarks[1])  # Chin to nose tip
    features["chin_angle"] = calculate_angle(landmarks[152], landmarks[1], landmarks[10])  # Chin, nose, forehead
    features["mouth_width"] = calculate_distance(landmarks[61], landmarks[291])  # Left to right mouth corner
    features["mouth_height"] = calculate_distance(landmarks[13], landmarks[14])  # Upper to lower lip
    
    return features

    # Example: Chin features
    features["chin_to_nose"] = calculate_distance(landmarks[152], landmarks[1])  # Chin to nose tip
    features["chin_angle"] = calculate_angle(landmarks[152], landmarks[1], landmarks[10])  # Chin, nose, forehead

    # Example: Smile features
    features["mouth_width"] = calculate_distance(landmarks[61], landmarks[291])  # Left to right mouth corner
    features["mouth_height"] = calculate_distance(landmarks[13], landmarks[14])  # Upper to lower lip
    
    return features

df["features"] = df["landmarks"].apply(extract_features)

# Convert feature dictionary to separate columns
df_features = df["features"].apply(pd.Series)

# Merge with labels
df_final = pd.concat([df[["label"]], df_features], axis=1)

# Save the processed dataset
df_final.to_csv("processed_features.csv", index=False)
print("Feature engineering complete. Saved to processed_features.csv")
