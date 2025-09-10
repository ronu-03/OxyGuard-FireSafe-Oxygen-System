import tkinter as tk
from tkinter import messagebox
import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Function to play fire alert sound
def play_fire_alert():
    try:
        pygame.mixer.music.load("fire_detected_alert.wav.wav")
        pygame.mixer.music.play()
    except Exception as e:
        print("Fire alert sound failed:", e)

# Logic for system status
def run_system_check():
    fire = fire_var.get()
    occupant = occupant_var.get()
    air_quality = air_var.get()

    if fire:
        status_label.config(text="🔥 FIRE DETECTED! Oxygen Valve Disabled!", fg="red")
        play_fire_alert()
        messagebox.showwarning("Danger", "FIRE DETECTED! Oxygen valve locked for safety.")
    elif occupant and air_quality:
        status_label.config(text="🚨 Supplying Oxygen...", fg="blue")
        pygame.mixer.music.stop()  # No sound needed
    else:
        status_label.config(text="✅ System Normal", fg="green")
        pygame.mixer.music.stop()

# GUI Setup
root = tk.Tk()
root.title("OxyGuard - Fire-Safe Oxygen System")
root.geometry("430x320")
root.configure(bg="white")

tk.Label(root, text="🔥 OxyGuard - Smart Oxygen Control System", font=("Arial", 13, "bold"), bg="white").pack(pady=10)

# Checkboxes
fire_var = tk.IntVar()
occupant_var = tk.IntVar()
air_var = tk.IntVar()

tk.Checkbutton(root, text="Fire Detected", variable=fire_var, font=("Arial", 11), bg="white").pack()
tk.Checkbutton(root, text="Occupant Present", variable=occupant_var, font=("Arial", 11), bg="white").pack()
tk.Checkbutton(root, text="Poor Air Quality", variable=air_var, font=("Arial", 11), bg="white").pack()

# Run Button
tk.Button(root, text="Run System Check", command=run_system_check,
          font=("Arial", 11), bg="#007BFF", fg="white").pack(pady=10)

# Status Display
status_label = tk.Label(root, text="✅ System Normal", font=("Arial", 12), bg="white", fg="green")
status_label.pack(pady=10)

root.mainloop()
