# 🎯 AI-Based Multi-Student Face Recognition Attendance System

An intelligent attendance management system that uses **Computer Vision** and **Face Recognition** to automatically identify students and record attendance in real time.

Developed using **Python, OpenCV, Face Recognition, and Tkinter**, this project eliminates manual attendance tracking and improves efficiency through automated face-based identification.

---

## 🚀 Features

✅ Real-Time Face Detection

✅ Multi-Student Face Recognition

✅ Automatic Attendance Marking

✅ Duplicate Attendance Prevention

✅ Photo Evidence Capture

✅ CSV-Based Attendance Records

✅ User-Friendly Tkinter GUI

✅ Automatic Student Loading from Images Folder

---

## 🖥️ GUI Preview

### Main Interface

![GUI Screenshot](screenshots/gui.png)

### Face Recognition

![Recognition Screenshot](screenshots/recognition.png)

### Attendance Record

![Attendance Screenshot](screenshots/attendance.png)

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| OpenCV | Camera Access & Image Processing |
| Face Recognition | Face Detection & Recognition |
| dlib | Facial Feature Encoding |
| Tkinter | Graphical User Interface |
| CSV | Attendance Storage |
| OS Module | File Management |

---

## 📂 Project Structure

```plaintext
AI-Face-Attendance-System/
│
├── gui.py
├── multi_attendance.py
├── attendance.csv
├── requirements.txt
├── README.md
│
├── images/
│   ├── Student1.jpg
│   ├── Student2.jpg
│   └── Student3.jpg
│
├── attendance_photos/
│
└── screenshots/
    ├── gui.png
    ├── recognition.png
    └── attendance.png
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Face-Attendance-System.git
```

### Move Into Project Folder

```bash
cd AI-Face-Attendance-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python gui.py
```

---

## 📸 How It Works

1. Load registered student images from the `images` folder.
2. Start webcam through GUI.
3. Detect and recognize faces in real time.
4. Match detected faces with stored student images.
5. Automatically mark attendance.
6. Save attendance data in `attendance.csv`.
7. Capture and store photo evidence.

---

## 📊 Example Attendance Record

| Name | Date | Time |
|--------|--------|--------|
| Ishra Kulsum | 2026-06-22 | 10:15:20 |
| Afra Tarannum | 2026-06-22 | 10:15:35 |
| Ashwini B | 2026-06-22 | 10:16:04 |

---

## 🔮 Future Enhancements

- Database Integration (MySQL / SQLite)
- Cloud-Based Attendance Storage
- Email Notifications
- Face Mask Detection
- Exam Proctoring Features
- Attendance Analytics Dashboard
- Student Registration Portal

---


## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
