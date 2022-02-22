import tkinter as tk
import threading

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
        self.detail = 0.9
        self.scale = 99
    def callback(self):
        self.root.quit()
    
    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.w1 = tk.Scale(self.root, from_=1, to=600)
        self.w1.pack()
        self.w2 = tk.Scale(self.root, from_=5, to=200)
        self.w2.set(100)
        self.w2.pack()
        self.detail = self.w1.get()
        self.root.mainloop()

    def get_detail(self):
        if self.detail > 0.9:
            return self.w1.get()
        return self.detail

    def get_scale(self):
        if self.scale !=100:
            return self.w2.get()
        return self.scale