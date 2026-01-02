# Bobby Orb: Floating Desktop Widget (Tkinter)
import tkinter as tk
from tkinter import simpledialog
import threading
import requests


class BobbyOrb(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bobby Orb')
        self.geometry('120x120+100+100')
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        self.configure(bg='black')
        self.canvas = tk.Canvas(self, width=120, height=120, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        self.orb = self.canvas.create_oval(10, 10, 110, 110, fill='#00e6e6', outline='#00ffff', width=4)
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        self.offset_x = 0
        self.offset_y = 0
        self.input_text = ''
        self.response_text = ''
        self.text_id = self.canvas.create_text(60, 60, text='B', fill='white', font=('Arial', 36, 'bold'))

        # Agent menu
        self.agent_menu = tk.Menu(self, tearoff=0)
        self.agents = [
            ('Noizy Brain', self.open_input_dialog),
            ('Voice Command', lambda: self.agent_action('voice_command')),
            ('Notifications', lambda: self.agent_action('notification')),
            ('Collaboration', lambda: self.agent_action('collab_tools')),
            ('Asset Manager', lambda: self.agent_action('asset_manager')),
            ('Dashboard', lambda: self.agent_action('dashboard_analytics')),
        ]
        for name, cmd in self.agents:
            self.agent_menu.add_command(label=name, command=cmd)
        self.canvas.bind('<Button-3>', self.show_agent_menu)

    def show_agent_menu(self, event):
        self.agent_menu.tk_popup(event.x_root, event.y_root)

    def on_click(self, event):
        self.offset_x = event.x
        self.offset_y = event.y
        # On double-click, open input dialog
        if event.type == tk.EventType.ButtonPress and event.num == 1:
            self.after(100, self.check_double_click, event)

    def check_double_click(self, event):
        if self.canvas.bind('<Double-Button-1>'):
            self.open_input_dialog()

    def on_drag(self, event):
        x = self.winfo_pointerx() - self.offset_x
        y = self.winfo_pointery() - self.offset_y
        self.geometry(f'+{x}+{y}')

    def open_input_dialog(self):
        user_input = simpledialog.askstring('Bobby Input', 'Ask Bobby anything:')
        if user_input:
            self.input_text = user_input
            self.canvas.itemconfig(self.text_id, text='...')
            threading.Thread(target=self.send_to_noizy_brain, args=(user_input,), daemon=True).start()

    def send_to_noizy_brain(self, query):
        try:
            url = 'http://localhost:5000/ask'
            resp = requests.post(url, json={'query': query})
            if resp.ok:
                answer = resp.json().get('answer', 'No response')
            else:
                answer = 'Error: Noizy Brain offline'
        except Exception as e:
            answer = f'Error: {e}'
        self.response_text = answer
        self.after(0, lambda: self.canvas.itemconfig(self.text_id, text='✓'))
        self.after(2000, lambda: self.canvas.itemconfig(self.text_id, text='B'))
        self.after(100, lambda: self.show_popup(answer))

    def agent_action(self, agent_name):
        # Generalized agent action (stub: can be expanded for each agent)
        user_input = simpledialog.askstring(f'{agent_name} Input', f'Command for {agent_name}:')
        if user_input:
            threading.Thread(target=self.send_to_agent, args=(agent_name, user_input), daemon=True).start()

    def send_to_agent(self, agent_name, query):
        try:
            url = f'http://localhost:5000/ask'
            resp = requests.post(url, json={'query': query, 'agent': agent_name})
            if resp.ok:
                answer = resp.json().get('answer', 'No response')
            else:
                answer = f'Error: {agent_name} offline'
        except Exception as e:
            answer = f'Error: {e}'
        self.after(100, lambda: self.show_popup(answer))

    def show_popup(self, text):
        popup = tk.Toplevel(self)
        popup.overrideredirect(True)
        popup.geometry(f'+{self.winfo_x()+130}+{self.winfo_y()}')
        label = tk.Label(popup, text=text, bg='white', fg='black', font=('Arial', 12), wraplength=300)
        label.pack(ipadx=10, ipady=10)
        popup.after(4000, popup.destroy)

if __name__ == '__main__':
    app = BobbyOrb()
    app.mainloop()
