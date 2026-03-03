import tkinter as tk
from tkinter import colorchooser, filedialog

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графіка")
        
        self.current_color = "black"
        self.tool = "pencil" # pencil, line, circle
        self.start_x = None
        self.start_y = None
        self.current_shape = None

        controls_frame = tk.Frame(root)
        controls_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Button(controls_frame, text="Олівець", command=lambda: self.set_tool("pencil")).pack(side=tk.LEFT, padx=5)
        tk.Button(controls_frame, text="Лінія", command=lambda: self.set_tool("line")).pack(side=tk.LEFT, padx=5)
        tk.Button(controls_frame, text="Коло", command=lambda: self.set_tool("circle")).pack(side=tk.LEFT, padx=5)
        tk.Button(controls_frame, text="Колір", command=self.choose_color).pack(side=tk.LEFT, padx=5)
        tk.Button(controls_frame, text="Очистити", command=self.clear_canvas).pack(side=tk.LEFT, padx=5)
        tk.Button(controls_frame, text="Зберегти .ps", command=self.save_image).pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def set_tool(self, tool):
        self.tool = tool

    def choose_color(self):
        color = colorchooser.askcolor(color=self.current_color)[1]
        if color:
            self.current_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".ps",
                                                 filetypes=[("PostScript", "*.ps")])
        if file_path:
            self.canvas.postscript(file=file_path, colormode='color')

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_drag(self, event):
        if self.tool == "pencil":
             self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.current_color, width=2)
             self.start_x = event.x
             self.start_y = event.y
        else:
            if self.current_shape:
                self.canvas.delete(self.current_shape)
            
            if self.tool == "line":
                self.current_shape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.current_color, width=2)
            elif self.tool == "circle":
                self.current_shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.current_color, width=2)

    def on_button_release(self, event):
        self.current_shape = None

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()