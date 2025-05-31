import tkinter as tk
import math

class HeartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💗 Looping Heart Fill Animation")
        self.root.geometry("600x1000")

        self.canvas = tk.Canvas(root, bg='white')
        self.canvas.pack(fill="both", expand=True)

        self.fill_steps = []
        self.step_index = 0
        self.scale = 60  # Controls heart size (~300x300)

        self.canvas.bind("<Configure>", self.on_resize)

    def generate_heart_fill_steps(self, center_x, center_y, scale):
        self.fill_steps = []
        for y_offset in range(-15 * scale, 15 * scale, 1):
            row = []
            for x_offset in range(-17 * scale, 17 * scale, 1):
                x = x_offset / scale
                y = -y_offset / scale
                if ((x**2 + y**2 - 1)**3 - x**2 * y**3) <= 0:
                    row.append((center_x + x_offset, center_y + y_offset))
            if row:
                self.fill_steps.append(row)

    def fill_heart_step(self):
        if self.step_index < len(self.fill_steps):
            row = self.fill_steps[self.step_index]
            for x, y in row:
                self.canvas.create_rectangle(x, y, x+1, y+1, fill="red", outline="red")
            self.step_index += 1
            self.root.after(10, self.fill_heart_step)
        else:
            # Restart animation after a short pause
            self.root.after(500, self.start_animation)

    def start_animation(self):
        self.canvas.delete("all")
        self.step_index = 0
        self.fill_heart_step()

    def draw_full_heart(self):
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        center_x = width // 2
        center_y = height // 2
        self.generate_heart_fill_steps(center_x, center_y, self.scale)
        self.start_animation()

    def on_resize(self, event):
        self.draw_full_heart()

root = tk.Tk()
app = HeartApp(root)
root.mainloop()
