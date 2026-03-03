import tkinter as tk
from logic import reverse_text, count_characters, to_upper

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Модульний додаток")
        self.root.geometry("400x300")

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.btn_reverse = tk.Button(root, text="Реверс", command=self.on_reverse)
        self.btn_reverse.pack(pady=5)

        self.btn_count = tk.Button(root, text="Кількість символів", command=self.on_count)
        self.btn_count.pack(pady=5)

        self.btn_upper = tk.Button(root, text="Верхній регістр", command=self.on_upper)
        self.btn_upper.pack(pady=5)

        self.result_label = tk.Label(root, text="Результат: ")
        self.result_label.pack(pady=20)

    def on_reverse(self):
        text = self.entry.get()
        result = reverse_text(text)
        self.result_label.config(text=f"Результат: {result}")

    def on_count(self):
        text = self.entry.get()
        result = count_characters(text)
        self.result_label.config(text=f"Результат: {result}")

    def on_upper(self):
        text = self.entry.get()
        result = to_upper(text)
        self.result_label.config(text=f"Результат: {result}")