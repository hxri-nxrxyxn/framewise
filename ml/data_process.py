import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

# settings for image
IMG_SIZE = 64  # all images resized to 64x64
DATA_DIR = "data"  # directory of collected data
CATEGORIES = ["happy", "sad", "neutral", "chin_up", "chin_down", "smile", "no_smile"]

# images and labels loaded
def load_data():
    X, y = [], []
    label_map = {category: i for i, category in enumerate(CATEGORIES)}

    for category in CATEGORIES:
        path = os.path.join(DATA_DIR, category)
        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)  # image in RGB
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))  # image resized to required
            img = img / 255.0  # pixel values are normalized
            X.append(img)
            y.append(label_map[category])

    return np.array(X), np.array(y)

X, y = load_data() # dataset loaded


# training and testing split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Dataset Loaded: {len(X_train)} training samples, {len(X_test)} testing samples")
