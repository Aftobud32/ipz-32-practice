import tkinter as tk
from tkinter import messagebox

def save_data():
    name = name_var.get()
    gender = gender_var.get()
    agreed = agree_var.get()

    if not agreed:
        result_label.config(text="Ви повинні погодитися з умовами!", fg="red")
        return

    result_text = f"Ім'я: {name}\nСтать: {gender}\nЗгода: Так"
    result_label.config(text=result_text, fg="black")

root = tk.Tk()
root.title("Анкета користувача")
root.geometry("400x300")

# Name
tk.Label(root, text="Ім'я:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_var = tk.StringVar()
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Gender
tk.Label(root, text="Стать:").grid(row=1, column=0, padx=10, pady=5, sticky="ne")
gender_frame = tk.Frame(root)
gender_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar(value="Чоловіча")
tk.Radiobutton(gender_frame, text="Чоловіча", variable=gender_var, value="Чоловіча").pack(anchor="w")
tk.Radiobutton(gender_frame, text="Жіноча", variable=gender_var, value="Жіноча").pack(anchor="w")

# Agreement
agree_var = tk.BooleanVar()
tk.Checkbutton(root, text="Погоджуюсь із умовами", variable=agree_var).grid(row=2, column=0, columnspan=2, pady=10)

# Save Button
tk.Button(root, text="Зберегти", command=save_data).grid(row=3, column=0, columnspan=2, pady=10)

# Result Display
result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()