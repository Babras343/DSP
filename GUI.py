# GUI.py
import tkinter as tk
from PIL import Image, ImageTk

class SpeedRotationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Speed and Rotation Detection")

        # Create labels for speeds and rotation
        self.speed_label = tk.Label(master, text="Speed:")
        self.speed_label.grid(row=0, column=0, padx=10, pady=10)

        self.rotation_label = tk.Label(master, text="Rotation:")
        self.rotation_label.grid(row=1, column=0, padx=10, pady=10)

        # Create a canvas for the traffic light
        self.traffic_light_canvas = tk.Canvas(master, width=30, height=70)
        self.traffic_light_canvas.grid(row=0, column=1, padx=10, pady=10)

        # Create arrows for rotation
        self.left_arrow = tk.Label(master, text="←")
        self.left_arrow.grid(row=1, column=1, padx=10, pady=10)

        self.right_arrow = tk.Label(master, text="→")
        self.right_arrow.grid(row=1, column=2, padx=10, pady=10)

    def update_values(self, speed, rotation):
        # Update the displayed values for speed
        self.speed_label.config(text=f"Speed: {speed}")

        # Update the traffic light based on speed
        self.traffic_light_canvas.delete("all")  # Clear previous drawing
        if speed == "Fast":
            self.traffic_light_canvas.create_oval(5, 5, 25, 25, fill='red')
        elif speed == "Slow":
            self.traffic_light_canvas.create_oval(5, 35, 25, 55, fill='yellow')
        elif speed == "Stopped":
            self.traffic_light_canvas.create_oval(5, 65, 25, 85, fill='green')

        # Update the arrows based on rotation
        if rotation == "Left":
            self.left_arrow.config(fg='blue')  # Change color or style as needed
            self.right_arrow.config(fg='black')
        elif rotation == "Right":
            self.left_arrow.config(fg='black')
            self.right_arrow.config(fg='blue')  # Change color or style as needed


async def run_GUI():
    root = tk.Tk()
    gui = SpeedRotationGUI(root)
    root.mainloop()
