# 🟢 Neo TextWriter

A minimal, retro-styled text editor and diary application written in Python using Tkinter.  
Inspired by Matrix/terminal aesthetics with green text on black background.

The project consists of two applications:

- **main.py** – Log Notepad (timestamped log files)
- **dagbog.py** – Daily Diary Writer (one file per day)

Both apps are lightweight, keyboard-driven, and designed for fast personal note-taking.

---

## ✨ Features

### main.py – Neo Log Notepad
- Green-on-black retro UI
- Create new log files with timestamp: `YYYY-MM-DD_HH-MM-SS.txt`
- Save and edit `log.txt`
- Fullscreen mode
- Zoom text in/out
- Clipboard support (copy, cut, paste)
- Keyboard shortcuts
- Menu system (File / Edit / View)

### dagbog.py – Neo Diary
- One diary file per day: `dagbog-YYYY-MM-DD.txt`
- Automatically loads today’s diary
- Retro UI (Matrix style)
- Help window with shortcuts
- Fullscreen support
- Zoom text
- Clipboard support
- Keyboard-focused workflow

---

## ⌨️ Keyboard Shortcuts

### Common shortcuts (both apps)

| Shortcut | Action |
|----------|--------|
| Ctrl + D | Insert current date |
| Ctrl + T | Insert current time |
| Ctrl + C | Copy |
| Ctrl + X | Cut |
| Ctrl + V | Paste |
| Ctrl + A | Select all |
| Ctrl + + | Increase font size |
| Ctrl + - | Decrease font size |
| F11 | Toggle fullscreen |

### main.py only

| Shortcut | Action |
|----------|--------|
| Ctrl + N | New log file (timestamp) |

### dagbog.py only

| Shortcut | Action |
|----------|--------|
| Ctrl + H | Show help window |

---

## 📁 File Structure

```
.
├── main.py
├── dagbog.py
├── log.txt
├── dagbog-YYYY-MM-DD.txt
├── background.png (optional)
└── README.md
```

---

## ▶️ How to Run

Requirements:
- Python 3.x
- Tkinter (usually included with Python)

Run log editor:
```bash
python3 main.py
```

Run diary writer:
```bash
python3 dagbog.py
```

---

## 🎨 Design Philosophy

- Minimal UI
- Keyboard-first workflow
- No distractions
- Retro terminal look
- Plain text files (future-proof)
- Works offline
- Linux friendly

---

## 🔮 Future Ideas

- Autosave
- Status bar (time + filename)
- Search in all logs/diaries
- Archive browser
- Encryption (password protected diary)
- Tabs (log + diary in one app)
- Export to PDF / Markdown

---

## 🧑‍💻 Author

Created as a personal journaling and logging tool using Python and Tkinter.  
Designed for simplicity, speed, and retro aesthetics.
