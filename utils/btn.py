import sys
from tkinter import *
from tkinter import ttk
import subprocess


def download_model():
    try:
        from huggingface_hub import snapshot_download
    except:
        subprocess.check_call([sys.executable, '-m', 'pip', 'intall', '--upgrade', 'huggingface_hub'])
        from huggingface_hub import snapshot_download
    
    return


# def get_selected_values():
    
#     selected_values['model'] = combobox_models.get()
#     selected_values['qt'] = combobox_qt.get()
#     print(selected_values)
#     return selected_values