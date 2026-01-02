# Bobby Orb: Floating Desktop Widget (Tkinter)
import tkinter as tk
from tkinter import simpledialog


import threading
import requests
import pvporcupine
import pyaudio
from PIL import Image, ImageTk




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
        # Try to load custom icon
        try:
            icon_path = 'bobby.png'  # Place your icon in the same directory as this script
            print(f"[Bobby Orb] Loading icon: {icon_path}")
            self.icon_img_normal = Image.open(icon_path).resize((100, 100), Image.ANTIALIAS)
            # Create a brightened version for animation
            enhancer = Image.new('RGBA', self.icon_img_normal.size, (255,255,200,60))
            self.icon_img_bright = Image.blend(self.icon_img_normal.convert('RGBA'), enhancer, 0.4)
            self.tk_icon_img_normal = ImageTk.PhotoImage(self.icon_img_normal)
            self.tk_icon_img_bright = ImageTk.PhotoImage(self.icon_img_bright)
            # Aura: create a soft glow image
            self.aura_img = Image.new('RGBA', (120, 120), (0,0,0,0))
            from PIL import ImageDraw
            draw = ImageDraw.Draw(self.aura_img)
            for r in range(50, 61, 2):
                alpha = int(60 * (1 - (r-50)/11))
                draw.ellipse((60-r, 60-r, 60+r, 60+r), fill=(255, 220, 100, alpha))
            self.tk_aura_img = ImageTk.PhotoImage(self.aura_img)
            self.aura = self.canvas.create_image(60, 60, image=self.tk_aura_img)
            self.orb = self.canvas.create_image(60, 60, image=self.tk_icon_img_normal)
            self.pulse_phase = 0
            self.pulse_animating = True
            self.after(0, self.animate_pulse)
            print("[Bobby Orb] Icon loaded and animation started.")
        except Exception as e:
            import traceback
            print(f"[Bobby Orb] Could not load custom icon: {e}")
            traceback.print_exc()
            self.orb = self.canvas.create_oval(10, 10, 110, 110, fill='#00e6e6', outline='#00ffff', width=4)
    def animate_pulse(self):
        # Animate aura pulse (idle breathing effect)
        if hasattr(self, 'aura'):
            import math
            self.pulse_phase = (self.pulse_phase + 1) % 60
            scale = 1.0 + 0.07 * math.sin(self.pulse_phase * math.pi / 30)
            self.canvas.coords(self.aura, 60, 60)
            self.canvas.itemconfig(self.aura, image=self.tk_aura_img)
            self.canvas.scale(self.aura, 60, 60, scale, scale)
        if self.pulse_animating:
            self.after(50, self.animate_pulse)
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
            ('Premium Dashboard', lambda: self.agent_action('premium_dashboard')),
        ]
        for name, cmd in self.agents:
            self.agent_menu.add_command(label=name, command=cmd)
        self.agent_menu.add_separator()
        self.agent_menu.add_command(label='Help/About', command=self.show_about)
        self.canvas.bind('<Button-3>', self.show_agent_menu)

        # Wake word detection thread (robust, fallback to text input if error)
        self.wake_word_active = True
        try:
            print("[Bobby Orb] Starting wake word thread...")
            self.wake_word_thread = threading.Thread(target=self.wake_word_listener, daemon=True)
            self.wake_word_thread.start()
        except Exception as e:
            import traceback
            print(f"[Bobby Orb] Wake word thread failed: {e}")
            traceback.print_exc()
            self.show_popup("Voice activation unavailable. Double-click or right-click to interact.")

    def wake_word_listener(self):
        try:
            print("[Bobby Orb] Initializing Porcupine for wake word...")
            porcupine = pvporcupine.create(keywords=["porcupine"])
        except Exception as e:
            import traceback
            msg = f"[Bobby Orb] Porcupine init failed: {e}"
            print(msg)
            traceback.print_exc()
            self.after(0, lambda: self.show_popup(msg))
            return
        try:
            print("[Bobby Orb] Initializing PyAudio for wake word...")
            pa = pyaudio.PyAudio()
            stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length)
        except Exception as e:
            import traceback
            msg = f"[Bobby Orb] PyAudio init failed: {e}"
            print(msg)
            traceback.print_exc()
            self.after(0, lambda: self.show_popup(msg))
            return
        try:
            print("[Bobby Orb] Wake word listening started.")
            while self.wake_word_active:
                try:
                    pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
                    pcm = memoryview(pcm).cast('h')
                    result = porcupine.process(pcm)
                    if result >= 0:
                        print("[Bobby Orb] Wake word detected!")
                        self.after(0, self.on_wake_word)
                except Exception as e:
                    import traceback
                    msg = f"[Bobby Orb] Wake word listen error: {e}"
                    print(msg)
                    traceback.print_exc()
                    self.after(0, lambda: self.show_popup(msg))
                    break
        finally:
            try:
                stream.stop_stream()
                stream.close()
                pa.terminate()
            except Exception as e:
                print(f"[Bobby Orb] Error closing audio stream: {e}")

    def on_wake_word(self):
        # Animate orb and open input dialog
        self.animate_listening()
        self.open_input_dialog()

    def animate_listening(self):
        # Animate orb: brighten and intensify aura
        try:
            self.pulse_animating = False
            self.canvas.itemconfig(self.orb, image=self.tk_icon_img_bright)
            # Temporarily make aura brighter
            aura_bright = self.aura_img.copy()
            from PIL import ImageEnhance
            enhancer = ImageEnhance.Brightness(aura_bright)
            aura_bright = enhancer.enhance(1.7)
            tk_aura_bright = ImageTk.PhotoImage(aura_bright)
            self.canvas.itemconfig(self.aura, image=tk_aura_bright)
            def reset():
                self.canvas.itemconfig(self.orb, image=self.tk_icon_img_normal)
                self.canvas.itemconfig(self.aura, image=self.tk_aura_img)
                self.pulse_animating = True
                self.after(0, self.animate_pulse)
            self.after(1000, reset)
        except Exception:
            # Fallback: flash text
            self.canvas.itemconfig(self.text_id, text='👂')
            self.after(500, lambda: self.canvas.itemconfig(self.text_id, text='B'))
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
            ('Premium Dashboard', lambda: self.agent_action('premium_dashboard')),
        ]
        for name, cmd in self.agents:
            self.agent_menu.add_command(label=name, command=cmd)
        self.agent_menu.add_separator()
        self.agent_menu.add_command(label='Help/About', command=self.show_about)
        self.canvas.bind('<Button-3>', self.show_agent_menu)

    def show_about(self):
        about = (
            "Bobby Orb\n"
            "NoizyFish Empire Desktop Assistant\n\n"
            "Right-click for agent menu.\n"
            "Double-click for Noizy Brain.\n"
            "Agents: Voice, Notifications, Collaboration, Asset Manager, Dashboard, Premium Dashboard.\n\n"
            "2025 NoizyFish. All rights reserved."
        )
        self.show_popup(about)

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
