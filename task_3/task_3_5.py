import tkinter as tk
from tkinter import ttk, colorchooser
import os

SETTINGS_FILE = "settings_3_5.txt"

def load_color():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return f.read().strip()
    return "#FFFFFF"

def save_color(color):
    with open(SETTINGS_FILE, "w") as f:
        f.write(color)

def update_bg(color):
    tab_main.config(bg=color)
    tab_settings.config(bg=color)
    tab_about.config(bg=color)

def choose_color():
    color_code = colorchooser.askcolor(title="Виберіть колір")[1]
    if color_code:
        save_color(color_code)
        update_bg(color_code)

root = tk.Tk()
root.title("Завдання 3.5 Вкладки")
root.geometry("400x300")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

tab_main = tk.Frame(notebook)
notebook.add(tab_main, text="Головна")
tk.Label(tab_main, text="Введіть дані:", bg=None).pack(pady=10)
tk.Entry(tab_main).pack(pady=5)

tab_settings = tk.Frame(notebook)
notebook.add(tab_settings, text="Налаштування")
tk.Button(tab_settings, text="Вибрати колір фону", command=choose_color).pack(pady=20)

tab_about = tk.Frame(notebook)
notebook.add(tab_about, text="Про програму")
tk.Label(tab_about, text="Автор: Назар Клокун\nГрупа: ІПЗ-32\nРік: 2026", bg=None).pack(pady=20)

current_color = load_color()
update_bg(current_color)

root.mainloop()