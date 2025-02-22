import os
import shutil
from sklearn.model_selection import train_test_split

OLD_DATA_DIR = "data_old"  
NEW_DATA_DIR = "data"      
CATEGORIES = ["happy", "sad", "neutral", "chin_up", "chin_down", "smile"]  

os.makedirs(f"{NEW_DATA_DIR}/train", exist_ok=True)
os.makedirs(f"{NEW_DATA_DIR}/validation", exist_ok=True)

for category in CATEGORIES:
    os.makedirs(f"{NEW_DATA_DIR}/train/{category}", exist_ok=True)
    os.makedirs(f"{NEW_DATA_DIR}/validation/{category}", exist_ok=True)

    img_dir = os.path.join(OLD_DATA_DIR, category)
    if not os.path.exists(img_dir):
        print(f"Warning: {img_dir} does not exist. Skipping.")
        continue

    imgs = [img for img in os.listdir(img_dir) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not imgs:
        print(f"Warning: No images found in {img_dir}. Skipping.")
        continue

    train_imgs, val_imgs = train_test_split(imgs, test_size=0.2, random_state=42)

    for img in train_imgs:
        src = os.path.join(OLD_DATA_DIR, category, img)
        dst = os.path.join(NEW_DATA_DIR, "train", category, img)
        shutil.copy(src, dst)

    for img in val_imgs:
        src = os.path.join(OLD_DATA_DIR, category, img)
        dst = os.path.join(NEW_DATA_DIR, "validation", category, img)
        shutil.copy(src, dst)

print("Dataset restructuring complete!")