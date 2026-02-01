from tkinter import *
import os
from datetime import datetime

BG = "black"
FG = "#00ff00"
FONT_FAMILY = "DejaVu Sans Mono"
font_size = 12
is_fullscreen = False

current_filename = "log.txt"

root = Tk()
root.title("Neo Log Notepad")
root.geometry("800x600")
root.configure(bg=BG)

text_area = Text(
    root,
    bg=BG,
    fg=FG,
    insertbackground=FG,
    font=(FONT_FAMILY, font_size),
    undo=True,
    borderwidth=0,
    highlightthickness=0
)
text_area.pack(expand=True, fill="both")

# --- Load or create log.txt ---
if os.path.exists(current_filename):
    with open(current_filename, "r") as f:
        text_area.insert("1.0", f.read())
else:
    with open(current_filename, "w") as f:
        f.write("")

# --- Save file ---
def save_file():
    with open(current_filename, "w") as f:
        f.write(text_area.get("1.0", END))

# --- New log file with datetime ---
def new_log_file(event=None):
    global current_filename
    save_file()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    current_filename = f"{timestamp}.txt"
    text_area.delete("1.0", END)
    text_area.insert(INSERT, f"[New log file: {current_filename}]\n")

# --- Insert date ---
def insert_date(event=None):
    text_area.insert(INSERT, datetime.now().strftime("%Y-%m-%d"))

# --- Insert time ---
def insert_time(event=None):
    text_area.insert(INSERT, datetime.now().strftime("%H:%M:%S"))

# --- Font size ---
def increase_font(event=None):
    global font_size
    font_size += 1
    text_area.config(font=(FONT_FAMILY, font_size))

def decrease_font(event=None):
    global font_size
    if font_size > 6:
        font_size -= 1
        text_area.config(font=(FONT_FAMILY, font_size))

# --- Fullscreen ---
def toggle_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    root.attributes("-fullscreen", is_fullscreen)

# --- Clipboard ---
def copy_text():
    try:
        root.clipboard_clear()
        root.clipboard_append(text_area.get("sel.first", "sel.last"))
    except:
        pass

def cut_text():
    try:
        copy_text()
        text_area.delete("sel.first", "sel.last")
    except:
        pass

def paste_text():
    try:
        text_area.insert(INSERT, root.clipboard_get())
    except:
        pass

def select_all(event=None):
    text_area.tag_add("sel", "1.0", "end")
    return "break"

# --- Help window ---
def show_help(event=None):
    help_win = Toplevel(root)
    help_win.title("Help - Shortcuts")
    help_win.configure(bg=BG)
    help_win.geometry("400x300")

    help_text = """
Shortcuts:

Ctrl+D   Insert date
Ctrl+T   Insert time
Ctrl+N   New log file

Ctrl+C   Copy
Ctrl+X   Cut
Ctrl+V   Paste
Ctrl+A   Select all

Ctrl +   Bigger text
Ctrl -   Smaller text

F11      Fullscreen
Ctrl+H   This help
"""

    label = Label(help_win, text=help_text, bg=BG, fg=FG,
                  font=(FONT_FAMILY, 11), justify="left")
    label.pack(padx=10, pady=10)

# --- Close ---
def on_close():
    save_file()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# --- Key bindings ---
root.bind("<Control-d>", insert_date)
root.bind("<Control-t>", insert_time)
root.bind("<Control-n>", new_log_file)

root.bind("<Control-plus>", increase_font)
root.bind("<Control-equal>", increase_font)
root.bind("<Control-minus>", decrease_font)

root.bind("<F11>", toggle_fullscreen)

root.bind("<Control-c>", lambda e: copy_text())
root.bind("<Control-x>", lambda e: cut_text())
root.bind("<Control-v>", lambda e: paste_text())
root.bind("<Control-a>", select_all)
root.bind("<Control-h>", show_help)

# --- Menu ---
menu = Menu(root, bg=BG, fg=FG, activebackground="#003300",
            activeforeground=FG, tearoff=0)
root.config(menu=menu)

file_menu = Menu(menu, bg=BG, fg=FG, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Log (Ctrl+N)", command=new_log_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_close)

edit_menu = Menu(menu, bg=BG, fg=FG, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)

view_menu = Menu(menu, bg=BG, fg=FG, tearoff=0)
menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Zoom In", command=increase_font)
view_menu.add_command(label="Zoom Out", command=decrease_font)
view_menu.add_command(label="Toggle Fullscreen", command=toggle_fullscreen)

help_menu = Menu(menu, bg=BG, fg=FG, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Shortcuts (Ctrl+H)", command=show_help)

root.mainloop()
