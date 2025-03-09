import cv2
import os

categories = ["happy", "sad", "neutral", "chin_up", "chin_down", "smile"] #categories for data collection

for category in categories:
    os.makedirs(f"data/{category}", exist_ok=True)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press the corresponding key to label and save an image:")
print("h - Happy, s - Sad, n - Neutral, u - Chin Up, d - Chin Down, m - Smile, x - No Smile, q - Quit")

counter = {cat: 0 for cat in categories}  #image count being tracked

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
        img_path = f"data/{category}/{counter[category]}.jpg"
        cv2.imwrite(img_path, frame)
        counter[category] += 1
        print(f"Saved: {img_path}")

cap.release()
cv2.destroyAllWindows()
