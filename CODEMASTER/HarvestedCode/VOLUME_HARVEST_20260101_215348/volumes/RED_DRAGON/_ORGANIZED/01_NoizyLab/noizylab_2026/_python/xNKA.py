import tkinter as tk
from tkinter import ttk

def set_volume(val):
    print(f"Volume set to: {val}")

root = tk.Tk()
root.title("Ernest Volume Slider")

slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=set_volume)
slider.set(50)
slider.pack(fill='x', padx=20, pady=20)

label = ttk.Label(root, text="Move the slider to set volume")
label.pack(pady=10)

root.mainloop()