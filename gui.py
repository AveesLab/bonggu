import sys
from tkinter import *
from tkinter import ttk
from utils.btn import *
from utils.tools import *



class BongGuGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("BongGu")
        self.geometry('400x300')
        self.resizable(False, False)
        
        self.model_list = ['LG-EXAONE', 'LLaMA2', 'LLaMA3']
        self.qt_list = ['f32', 'f16', 'bf16', 'q8_0', 'tq1_0', 'tq2_0', 'auto']
        self.mode_list = ['Basic', 'Conversation', 'Interactive']


        self.top_frame = Frame(self, relief = 'solid')
        self.top_frame.pack(side = 'top', fill = 'x')
        self.left_frame = Frame(self, relief = 'solid')
        self.left_frame.pack(side = 'left', fill = 'y')
        self.right_frame = Frame(self, relief = 'solid')
        self.right_frame.pack(side = 'right', fill = 'y')
        self.bottom_frame = Frame(self, relief = 'solid')
        self.bottom_frame.pack(side = 'bottom', fill = 'x')
        


        self.png = jpg_to_png('images/BongGu.JPG')
        self.label_img = Label(self.top_frame, image = self.png, text = 'BongGu', compound = 'left', font=("Helvetica", 32), padx = 40)
        self.label_img.pack(side = 'left')

        self.make_combobox(self.model_list, self.left_frame, "Model")
        self.make_combobox(self.qt_list, self.right_frame, "Quantization")
        self.make_combobox(self.mode_list, self.right_frame, "Mode")
        
        self.make_button(self.bottom_frame, "Start", download_model)
        self.make_button(self.bottom_frame, "Quit", self.quit_bonggu)
        bonggu_with_start()

    def quit_bonggu(self):
        bonggu_with_quit()
        self.destroy()

    def make_combobox(self, items, frame, name):
        label = Label(frame, text = name)
        label.pack()
        combobox = ttk.Combobox(frame, width = 10, height = 10, values = items)
        combobox.pack()
        combobox.set("(Select)")
    
    def make_button(self, frame, name, fn):
        btn = Button(frame, text = name, command = fn)
        btn.pack(side = LEFT, padx = 10)