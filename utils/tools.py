from PIL import Image, ImageTk


def jpg_to_png(path):
    jpg = Image.open(path)
    resized_jpg = jpg.resize((50, 50))
    png = ImageTk.PhotoImage(resized_jpg)
    return png # png

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

