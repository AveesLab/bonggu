import sys
from tkinter import *
from tkinter import ttk
from utils.btn import *

app = Tk()
app.title("BongGu")
app.geometry('400x300')
app.resizable(False, False)


selected_values = {'model' : "LG-EXAONE", 'qt' : 'q8_0'}

def get_selected_values():
    selected_values['model'] = combobox_models.get()
    selected_values['qt'] = combobox_qt.get()
    print(selected_values)
    return selected_values

# frame
frame_model = Frame(app, relief = 'solid')
frame_model.pack(side = 'left', fill = 'both', expand = True)

frame_qt = Frame(app, relief = 'solid')
frame_qt.pack(side = 'right', fill = 'both', expand = True)

frame_opt = Frame(app, relief = 'solid')
frame_opt.pack()

# label
label_model = Label(frame_model, text = 'Models')
label_model.pack()
label_qt = Label(frame_qt, text = "Quantization")
label_qt.pack()

# combo

model_list = ['LG-EXAONE', 'LLaMA2', 'LLaMA3']
combobox_models = ttk.Combobox(frame_model, width = 10, height = 10, values = model_list)
combobox_models.pack()
combobox_models.set('(Select)')


qt_type = ['f32', 'f16', 'bf16', 'q8_0', 'tq1_0', 'tq2_0', 'auto']
combobox_qt = ttk.Combobox(frame_qt, width = 10, height = 10, values = qt_type)
combobox_qt.pack()
combobox_qt.set('(Select)')
btn = Button(frame_opt, text = 'Start', command = download_model)
btn.pack()


# photoimage
# image = PhotoImage(file = 'images/BongGu.JPG')
# label_image = Label(app, text = 'img', image=image)
# label_image.pack()

app.mainloop()