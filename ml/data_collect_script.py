import cv2
import os
import glob

# Define categories for data collection
categories = ["happy", "sad", "neutral", "chin_up", "chin_down", "smile", "no_smile"]

# Create directories if they don't exist
for category in categories:
    os.makedirs(f"data/{category}", exist_ok=True)

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press the corresponding key to label and save an image:")
print("h - Happy, s - Sad, n - Neutral, u - Chin Up, d - Chin Down, m - Smile, x - No Smile, q - Quit")

def get_next_image_index(category):
    existing_files = glob.glob(f"data/{category}/*.jpg") #finds next available index to add data whenver
    
    if not existing_files:  
        return 0

    indices = [int(os.path.basename(f).split('.')[0]) for f in existing_files if f.split('/')[-1].split('.')[0].isdigit()] #extract the last index number
    
    return max(indices) + 1 if indices else 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    cv2.imshow("Press a key to label the image", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    key_map = {
        'h': "happy", 's': "sad", 'n': "neutral",
        'u': "chin_up", 'd': "chin_down", 'm': "smile", 'x': "no_smile"
    }

    if chr(key) in key_map:
        category = key_map[chr(key)]
        img_index = get_next_image_index(category)  
        img_path = f"data/{category}/{img_index}.jpg"
        cv2.imwrite(img_path, frame)
        print(f" Saved: {img_path}")

cap.release()
cv2.destroyAllWindows()
