import numpy as np
import pandas as pd
import joblib

rf_model_loaded = joblib.load("face_pose_model.pkl")

# Define column names (ensure they match your feature columns in X_train/X_test)
columns = ["chin_to_nose", "chin_angle", "mouth_width", "mouth_height"]

# Create a DataFrame with the new sample
new_sample = pd.DataFrame([[
    0.1668371165331815,  # chin_to_nose
    2.5772716080419515,   # chin_angle
    0.11660644718918717,  # mouth_width
    0.02706421113754928 # mouth_height
]], columns=columns)


# Predict using the trained model
prediction = rf_model_loaded.predict(new_sample)

print(f"Predicted Label: {prediction[0]}")
