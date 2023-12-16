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

        # Create labels to display the detected values
        self.speed_value = tk.StringVar()
        self.speed_display = tk.Label(master, textvariable=self.speed_value)
        self.speed_display.grid(row=0, column=1, padx=10, pady=10)

        self.rotation_value = tk.StringVar()
        self.rotation_display = tk.Label(master, textvariable=self.rotation_value)
        self.rotation_display.grid(row=1, column=1, padx=10, pady=10)

        # Create an image placeholder for a visualization (you can replace this with your actual visualization)
        self.image_path = "placeholder_image.png"
        self.image = ImageTk.PhotoImage(Image.open(self.image_path))
        self.image_label = tk.Label(master, image=self.image)
        self.image_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def update_values(self, speed, rotation):
        # Update the displayed values
        self.speed_value.set(speed)
        self.rotation_value.set(rotation)

        # Update the image (replace this with the actual visualization)
        new_image = ImageTk.PhotoImage(Image.open(self.image_path))
        self.image_label.configure(image=new_image)
        self.image_label.image = new_image

if __name__ == "__main__":
    root = tk.Tk()
    gui = SpeedRotationGUI(root)

    # Example: Update GUI with detected values
    detected_speed = "Fast"
    detected_rotation = "Right"
    gui.update_values(detected_speed, detected_rotation)

    root.mainloop()
