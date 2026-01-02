import tkinter as tk
from tkinter import simpledialog
import threading

class BobbyBubble:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bobby Says")
        self.root.geometry("400x150")
        self.root.resizable(False, False)
        self.text_var = tk.StringVar()
        self.label = tk.Label(self.root, textvariable=self.text_var, wraplength=380, font=("Arial", 14), justify="left")
        self.label.pack(pady=10, padx=10)
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(fill="x", padx=10)
        self.entry.bind("<Return>", self._on_enter)
        self.response = None
        self.root.withdraw()  # Hide initially

    def show_message(self, message):
        self.text_var.set(message)
        self.entry.delete(0, tk.END)
        self.response = None
        self.root.deiconify()
        self.entry.focus_set()
        self.root.lift()
        self.root.after(100, lambda: self.root.focus_force())
        self.root.update()

    def get_response(self, prompt):
        self.show_message(prompt)
        self.root.wait_variable(self.text_var)  # Wait until user enters response
        self.root.withdraw()
        return self.response

    def _on_enter(self, event):
        self.response = self.entry.get().strip()
        self.text_var.set("")  # This will break wait_variable

    def close(self):
        self.root.destroy()

# Example usage:
if __name__ == "__main__":
    bubble = BobbyBubble()
    def run():
        while True:
            msg = simpledialog.askstring("Speak to Bobby", "What should Bobby say?")
            if not msg:
                break
            bubble.show_message(msg)
            bubble.root.after(2000, bubble.root.withdraw)  # Auto-hide after 2s
    threading.Thread(target=run).start()
    bubble.root.mainloop()
