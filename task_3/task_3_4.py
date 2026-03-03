import tkinter as tk

def calculate(operation):
    try:
        val1 = float(entry1.get())
        val2 = float(entry2.get())
        result = 0
        
        if operation == "+":
            result = val1 + val2
        elif operation == "-":
            result = val1 - val2
        elif operation == "*":
            result = val1 * val2
        elif operation == "/":
            if val2 == 0:
                lbl_result.config(text="Помилка: Ділення на нуль")
                return
            result = val1 / val2
            
        lbl_result.config(text=f"Результат: {result}")
    except ValueError:
        lbl_result.config(text="Помилка: Некоректні дані")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x250")

tk.Label(root, text="Число 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Число 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="+", width=5, command=lambda: calculate("+")).grid(row=0, column=0)
tk.Button(btn_frame, text="-", width=5, command=lambda: calculate("-")).grid(row=0, column=1)
tk.Button(btn_frame, text="*", width=5, command=lambda: calculate("*")).grid(row=0, column=2)
tk.Button(btn_frame, text="/", width=5, command=lambda: calculate("/")).grid(row=0, column=3)

lbl_result = tk.Label(root, text="Результат: ")
lbl_result.pack(pady=10)

root.mainloop()