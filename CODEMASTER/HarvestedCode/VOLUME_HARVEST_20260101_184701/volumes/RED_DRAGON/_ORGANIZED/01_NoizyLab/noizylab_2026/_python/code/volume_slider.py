import tkinter as tk
from tkinter import ttk
import subprocess

def set_system_volume(val):
    # macOS system volume (0-100 mapped to 0-100)
    subprocess.run(['osascript', '-e', f'set volume output volume {int(float(val))}'])

def main():
    root = tk.Tk()
    root.title("Ernest Volume Slider")
    root.geometry("400x120")

    label = ttk.Label(root, text="Ernest Volume Slider", font=("Helvetica", 16, "bold"))
    label.pack(pady=10)

    slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=set_system_volume, length=350)
    slider.set(50)
    slider.pack(pady=10)

    value_label = ttk.Label(root, text="Volume: 50")
    value_label.pack()

    def update_label(val):
        value_label.config(text=f"Volume: {int(float(val))}")

    slider.config(command=lambda val: [set_system_volume(val), update_label(val)])

    root.mainloop()

if __name__ == "__main__":
    main() 