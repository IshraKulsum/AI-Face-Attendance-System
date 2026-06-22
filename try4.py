# ==========================================
# AI-Based Multi Student Face Attendance System

# ==========================================

import cv2
import face_recognition
import csv
import os
from datetime import datetime

# ==========================================
# Load All Student Images
# ==========================================

known_encodings = []
known_names = []

IMAGES_FOLDER = "images"

for filename in os.listdir(IMAGES_FOLDER):

    if filename.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):

        image_path = os.path.join(
            IMAGES_FOLDER,
            filename
        )

        image = face_recognition.load_image_file(
            image_path
        )

        encodings = face_recognition.face_encodings(
            image
        )

        if len(encodings) > 0:

            known_encodings.append(
                encodings[0]
            )

            student_name = (
                os.path.splitext(
                    filename
                )[0].replace(
                    "_",
                    " "
                )
            )

            known_names.append(
                student_name
            )

print(
    "Loaded Students:",
    known_names
)

# ==========================================
# Attendance File Setup
# ==========================================

FILE_NAME = "attendance.csv"

if not os.path.exists(FILE_NAME):

    with open(
        FILE_NAME,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Date",
            "Time"
        ])

# ==========================================
# Today's Date
# ==========================================

today = datetime.now().strftime(
    "%Y-%m-%d"
)

# Store students already marked today
marked_today = set()

# Load today's existing attendance
with open(
    FILE_NAME,
    "r"
) as file:

    reader = csv.reader(file)

    for row in reader:

        if len(row) >= 2:

            if row[1] == today:

                marked_today.add(
                    row[0]
                )

# ==========================================
# Create Photo Folder
# ==========================================

os.makedirs(
    "attendance_photos",
    exist_ok=True
)

# ==========================================
# Start Webcam
# ==========================================

cap = cv2.VideoCapture(0)

status_message = (
    "Waiting for face..."
)

print(
    "Camera Started..."
)

print(
    "Press Q to quit"
)

# ==========================================
# Main Loop
# ==========================================

while True:

    ret, frame = cap.read()

    if not ret:
        break

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    face_locations = (
        face_recognition.face_locations(
            rgb_frame
        )
    )

    face_encodings = (
        face_recognition.face_encodings(
            rgb_frame,
            face_locations
        )
    )

    for face_encoding, face_location in zip(
        face_encodings,
        face_locations
    ):

        matches = (
            face_recognition.compare_faces(
                known_encodings,
                face_encoding
            )
        )

        if True in matches:

            match_index = (
                matches.index(True)
            )

            NAME = (
                known_names[
                    match_index
                ]
            )

            top, right, bottom, left = (
                face_location
            )

            # Draw rectangle
            cv2.rectangle(
                frame,
                (left, top),
                (right, bottom),
                (0, 255, 0),
                2
            )

            # Display name
            cv2.putText(
                frame,
                NAME,
                (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            # Mark attendance once per day
            if NAME not in marked_today:

                current_time = (
                    datetime.now().strftime(
                        "%H:%M:%S"
                    )
                )

                with open(
                    FILE_NAME,
                    "a",
                    newline=""
                ) as file:

                    writer = csv.writer(
                        file
                    )

                    writer.writerow([
                        NAME,
                        today,
                        current_time
                    ])

                # Save photo evidence
                photo_name = (
                    f"attendance_photos/"
                    f"{NAME}_"
                    f"{current_time.replace(':', '-')}.jpg"
                )

                cv2.imwrite(
                    photo_name,
                    frame
                )

                marked_today.add(
                    NAME
                )

                status_message = (
                    f"{NAME} Marked Present"
                )

                print(
                    f"{NAME} marked present!"
                )

                print(
                    f"Photo saved: {photo_name}"
                )

    # Display status message
    cv2.putText(
        frame,
        status_message,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.imshow(
        "AI Multi Student Attendance System",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ==========================================
# Cleanup
# ==========================================

cap.release()
cv2.destroyAllWindows()
