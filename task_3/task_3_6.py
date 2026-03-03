import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Блокнот - Без назви")
        self.root.geometry("600x400")

        self.text_area = tk.Text(root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        self.current_file = None
        self.is_modified = False
        self.text_area.bind("<<Modified>>", self.on_modified)

        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Відкрити", command=self.open_file)
        file_menu.add_command(label="Зберегти", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Вийти", command=self.on_closing)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        root.config(menu=menu_bar)

        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_modified(self, event=None):
        if self.text_area.edit_modified():
            self.is_modified = True
            title = "Блокнот - " + (self.current_file if self.current_file else "Без назви") + "*"
            self.root.title(title)
            self.text_area.edit_modified(False)

    def open_file(self):
        if not self.check_unsaved():
            return
        
        file_path = filedialog.askopenfilename(filetypes=[("Текстові файли", "*.txt"), ("Всі файли", "*.*")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)
                self.current_file = file_path
                self.is_modified = False
                self.root.title(f"Блокнот - {file_path}")
                self.text_area.edit_modified(False)
            except Exception as e:
                messagebox.showerror("Помилка", str(e))

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(self.text_area.get(1.0, tk.END))
                self.is_modified = False
                self.root.title(f"Блокнот - {self.current_file}")
            except Exception as e:
                messagebox.showerror("Помилка", str(e))
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Текстові файли", "*.txt"), ("Всі файли", "*.*")])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(self.text_area.get(1.0, tk.END))
                self.current_file = file_path
                self.is_modified = False
                self.root.title(f"Блокнот - {file_path}")
            except Exception as e:
                messagebox.showerror("Помилка", str(e))

    def check_unsaved(self):
        if self.is_modified:
            response = messagebox.askyesnocancel("Незбережені зміни", "Ви хочете зберегти зміни?")
            if response is True:
                self.save_file()
                return True
            elif response is False:
                return True
            else:
                return False
        return True

    def on_closing(self):
        if self.check_unsaved():
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()