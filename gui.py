import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# ==========================
# Start Attendance System
# ==========================
def start_attendance():
    try:
        subprocess.run(
            ["python", "try4.py"],
            check=True
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

# ==========================
# View Attendance CSV
# ==========================
def view_attendance():

    if os.path.exists("attendance.csv"):

        os.startfile("attendance.csv")

    else:

        messagebox.showwarning(
            "Warning",
            "Attendance file not found!"
        )

# ==========================
# View Photos Folder
# ==========================
def view_photos():

    if os.path.exists("attendance_photos"):

        os.startfile("attendance_photos")

    else:

        messagebox.showwarning(
            "Warning",
            "Photo folder not found!"
        )

# ==========================
# Exit Application
# ==========================
def exit_app():
    root.destroy()

# ==========================
# Main Window
# ==========================
root = tk.Tk()

root.title("AI-Based Face Attendance System")

root.geometry("450x400")

# Heading
title = tk.Label(
    root,
    text="Fac Recognition Based Attendance System",
    font=("Arial", 16, "bold")
)

title.pack(pady=20)

# Developer Name
developer = tk.Label(
    root,
    text="Inter Disciplinary Project Based Learning",
    font=("Arial", 10)
)

developer.pack(pady=5)

# Start Camera Button
start_btn = tk.Button(
    root,
    text="Start Camera",
    width=20,
    height=2,
    command=start_attendance
)

start_btn.pack(pady=10)

# View Attendance Button
view_btn = tk.Button(
    root,
    text="View Attendance",
    width=20,
    height=2,
    command=view_attendance
)

view_btn.pack(pady=10)

# View Photos Button
photos_btn = tk.Button(
    root,
    text="View Photos",
    width=20,
    height=2,
    command=view_photos
)

photos_btn.pack(pady=10)

# Exit Button
exit_btn = tk.Button(
    root,
    text="Exit",
    width=20,
    height=2,
    command=exit_app
)

exit_btn.pack(pady=10)

# Run GUI
root.mainloop()