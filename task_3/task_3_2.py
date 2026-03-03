import tkinter as tk

def greet():
    label.config(text="Вітаю, користувач!")

def clear():
    label.config(text="")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Завдання 3.2")
root.geometry("300x250")

label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=20)

btn_greet = tk.Button(root, text="Привітати", command=greet)
btn_greet.pack(pady=5)

btn_clear = tk.Button(root, text="Очистити", command=clear)
btn_clear.pack(pady=5)

btn_exit = tk.Button(root, text="Вийти", command=exit_app)
btn_exit.pack(pady=5)

root.mainloop()