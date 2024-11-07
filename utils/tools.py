import sys, os
import subprocess
try:
    from PIL import Image, ImageTk
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    from PIL import Image, ImageTk

def jpg_to_png(path):
    jpg = Image.open(path)
    resized_jpg = jpg.resize((50, 50))
    png = ImageTk.PhotoImage(resized_jpg)
    return png # png

def check_dir(dir_path):
    if os.path.isdir(dir_path):
        return True
    else:
        return False
def check_file(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False

def bonggu_with_start():
    print("        ／￣￣￣￣＼         ███████  ████████   █████   ██████  ████████")
    print("      ／                 ＼       ██          ██       ██    ██  ██          ██    ")
    print("    ｜      ●      ●      ｜      █████     ██       ██    ██  ██          ██    ")
    print("    ｜      ◡      ◡      ｜      ██          ██       ██    ██  ██          ██    ")
    print("     ＼      ︶︶       ／       ██          ██        █████   ██████     ██    ")
    print("       ＼＿＿＿＿＿／ ")
    print("         ｜       ｜")
    print("       ／           ＼")
    print("      ｜｜       ｜｜")
    print("      ～～       ～～ ")

def bonggu_with_quit():
    print("        ／￣￣￣￣＼         ██████   ██    ██  ██  ████████")
    print("      ／                 ＼       ██    ██   ██  ██       ██   ")
    print("    ｜      ●      ●      ｜      ██████      ██         ██   ")
    print("    ｜      ◡      ◡      ｜      ██    ██    ██         ██   ")
    print("     ＼      ︶︶       ／       ██    ██    ██         ██   ")
    print("       ＼＿＿＿＿＿／          ██████     ██         ██   ")
    print("         ｜       ｜")
    print("       ／           ＼")
    print("      ｜｜       ｜｜")
    print("      ～～       ～～ ")

