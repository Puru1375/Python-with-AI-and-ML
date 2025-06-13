# encode_faces.py
import face_recognition
import pickle
import os
import cv2 # OpenCV for loading images potentially

print("[INFO] Starting face encoding...")
KNOWN_FACES_DIR = "known_faces"
ENCODINGS_FILE = "known_face_encodings.pkl"

# Initialize lists to store encodings and names
known_encodings = []
known_names = []

# Loop over the directories (each directory corresponds to a person)
for person_name in os.listdir(KNOWN_FACES_DIR):
    person_dir = os.path.join(KNOWN_FACES_DIR, person_name)

    # Check if it's actually a directory
    if not os.path.isdir(person_dir):
        continue

    print(f"[INFO] Processing images for {person_name}...")

    # Loop over the images in the person's directory
    for image_name in os.listdir(person_dir):
        image_path = os.path.join(person_dir, image_name)

        # Check if it's a file
        if not os.path.isfile(image_path):
            continue

        try:
            # Load the image using face_recognition (handles different formats)
            # It loads in RGB format, which is what face_recognition expects
            image = face_recognition.load_image_file(image_path)

            # Detect face locations (using CNN model for better accuracy, though slower)
            # Alternatively use model='hog' for faster but less accurate detection
            boxes = face_recognition.face_locations(image, model='cnn') # or 'hog'

            # Compute the facial embedding for the face
            # Assumes only ONE face per image for enrollment simplicity
            # If multiple faces, it encodes the first one found. Handle appropriately if needed.
            encodings = face_recognition.face_encodings(image, boxes)

            if len(encodings) > 0:
                # Use the first encoding found
                encoding = encodings[0]
                known_encodings.append(encoding)
                known_names.append(person_name)
                print(f"      Encoded {image_name} successfully.")
            else:
                print(f"[WARNING] No face found in {image_name}, skipping.")

        except Exception as e:
            print(f"[ERROR] Failed to process {image_path}: {e}")

# Save the known encodings and names to disk
print("[INFO] Saving encodings...")
data = {"encodings": known_encodings, "names": known_names}
with open(ENCODINGS_FILE, "wb") as f:
    pickle.dump(data, f)

print(f"[INFO] Encodings saved to {ENCODINGS_FILE}")
print("[INFO] Face encoding process complete.")