import os
import shutil

# Define the directory paths
downloaded_dir = "C:\\Users\\Chiraag\\Desktop\\Prodigy\\Task 4\\leapGestRecog"
formatted_dir = "C:\\Users\\Chiraag\\Desktop\\Prodigy\\Task 4\\Formatted Data"

# Create the formatted directory if it doesn't exist
if not os.path.exists(formatted_dir):
    os.makedirs(formatted_dir)

# Function to format the data
def format_data(original_dir, formatted_dir):
    for subject_folder in os.listdir(original_dir):
        subject_path = os.path.join(original_dir, subject_folder)
        if os.path.isdir(subject_path):
            formatted_subject_path = os.path.join(formatted_dir, subject_folder)
            os.makedirs(formatted_subject_path, exist_ok=True)
            print(f"Formatting subject: {subject_folder}")
            for gesture_folder in os.listdir(subject_path):
                gesture_path = os.path.join(subject_path, gesture_folder)
                if os.path.isdir(gesture_path):
                    formatted_gesture_path = os.path.join(formatted_subject_path, gesture_folder)
                    os.makedirs(formatted_gesture_path, exist_ok=True)
                    print(f"Moving files from {gesture_path} to {formatted_gesture_path}")
                    for image_file in os.listdir(gesture_path):
                        image_path = os.path.join(gesture_path, image_file)
                        print(f"Moving file: {image_path}")
                        shutil.move(image_path, formatted_gesture_path)

# Format the data
format_data(downloaded_dir, formatted_dir)

# Problem statement
print("""Hand Gesture Recognition Problem Statement:

Context:
Hand gesture recognition database is presented, composed by a set of near infrared images acquired by the Leap Motion sensor.

Content:
The database is composed by 10 different hand-gestures that were performed by 10 different subjects (5 men and 5 women).

The database is structured in different folders as:
- /00 (subject with identifier 00)
- /01_palm (images for palm gesture of subject 00)
- /02_l (images for l gesture of subject 00)
- ...
- /10_down (images for down gesture of subject 10)

Every root folder (00, 01,...) contains the infrared images of one subject. The folder name is the identifier of each different subject.

The objective is to develop a hand gesture recognition system using machine learning or deep learning techniques to accurately classify the hand gestures performed by the subjects.""")

