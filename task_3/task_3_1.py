import tkinter as tk

def close_app():
    root.destroy()

root = tk.Tk()
root.title("Перша програма")
root.geometry("1024x768")
root.resizable(False, False)

label = tk.Label(root, text="Привіт, світ!", font=("Arial", 24))
label.pack(pady=20)

button = tk.Button(root, text="Закрити", command=close_app)
button.pack(pady=20)

root.mainloop()