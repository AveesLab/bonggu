import sys
from tkinter import *
from tkinter import ttk
from utils.btn import *
from utils.tools import *


app = Tk()
app.title("BongGu")
app.geometry('400x300')
app.resizable(False, False)


selected_values = {'model' : "LG-EXAONE", 'qt' : 'q8_0'}


class BongGuGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("BongGu")
        self.geometry('600x400')









def get_selected_values():
    selected_values['model'] = combobox_models.get()
    selected_values['qt'] = combobox_qt.get()
    print(selected_values)
    return selected_values

def quit_bonggu():
    app.destroy()


def make_combobox(items, frame, name):
    label = Label(frame, text = name)
    label.pack()
    combobox = ttk.Combobox(frame, width = 10, height = 10, values = items)
    combobox.pack()
    combobox.set("(Select)")


frame_opt = Frame(app, relief = 'solid')
frame_opt.pack(side = 'top', fill = 'x')

frame_model = Frame(app, relief = 'solid')
frame_model.pack(side = 'left', fill = 'y', expand = True)

frame_qt = Frame(app, relief = 'solid')
frame_qt.pack(side = 'right', fill = 'y', expand = True)

frame_start = Frame(app, relief = 'solid')
frame_start.pack(side = 'left', fill = 'y')
frame_quit = Frame(app, relief = 'solid')
frame_quit.pack(side = 'right', fill = 'y')

png = jpg_to_png('images/BongGu.JPG')
label_img = Label(frame_opt, image = png, text = 'BongGu', compound = 'left', font=("Helvetica", 32), padx = 40)
label_img.pack(side = 'left')


model_list = ['LG-EXAONE', 'LLaMA2', 'LLaMA3']
qt_list = ['f32', 'f16', 'bf16', 'q8_0', 'tq1_0', 'tq2_0', 'auto']
mode_list = ['Basic', 'Conversation', 'Interactive']
make_combobox(model_list, frame_model, "Model")
make_combobox(qt_list, frame_qt, "Quantization")
make_combobox(mode_list, frame_qt, "Mode")



btn_start = Button(frame_start, text = 'Start', command = download_model)
btn_start.pack()
btn_quit = Button(frame_quit, text = 'Quit', command = quit_bonggu)
btn_quit.pack()


app.mainloop()