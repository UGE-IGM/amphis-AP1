import tkinter as tk
from tkinter import ttk
from tkinter import font
from sys import argv


class Euclid:
    def __init__(self, a, b, width=1000, height=500, margin_r=.05):
        self.a, self.b = int(a), int(b)
        if self.a < self.b:
            self.a, self.b = self.b, self.a
        self.curr_a, self.curr_b = self.a, self.b
        
        self.margin = margin_r * width
        self.scale = min((width - 2*self.margin) / self.a,
                         (height - 2*self.margin) / self.b)
        
        self.ul = self.margin, self.margin
        self.curr_ul = self.ul
        self.lr = (self.ul[0] + self.scale * self.a,
                   self.ul[1] + self.scale * self.b)
        
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root,
                                width=width, height=height,
                                bd=0, highlightthickness=0)
        self.canvas.grid(column=0, row=0, sticky='nsew')
        self.canvas.bind("<1>", self.divide_room)

        self.canvas.create_text(height-self.margin, width/2,
                                text=f"a = {self.a}, b = {self.b}",
                                tag="text", anchor="s", justify="center",
                                font=('Helvetica','30','bold'))

        self.draw_room()
        self.root.mainloop()

    def draw_room(self):
        self.canvas.create_rectangle(*self.ul, *self.lr)
        self.canvas.create_rectangle(*self.ul, *self.lr,
                                     tag="remainder", fill="grey")
        
    def divide_room(self, event):
        if self.curr_a == 0 or self.curr_b == 0:
            return
        x, y = self.curr_ul
        if self.curr_a > self.curr_b:
            q, r = divmod(self.curr_a, self.curr_b)
            bound = q + 1 if r > 0 else q
            dy = self.scale * self.curr_b
            for i in range(1, bound):
                xi = x + i * dy
                self.canvas.create_line(xi, y, xi, y+dy)
            self.curr_ul = x + q*dy, y
            self.curr_a, self.curr_b = r, self.curr_b
        else:
            q, r = divmod(self.curr_b, self.curr_a)
            bound = q + 1 if r > 0 else q
            dx = self.scale * self.curr_a
            for i in range(1, bound):
                yi = y + i * dx
                self.canvas.create_line(x, yi, x+dx, yi)
            self.curr_ul = x, y + q*dx
            self.curr_a, self.curr_b = self.curr_a, r
        self.canvas.delete("remainder")
        if self.curr_a > 0 and self.curr_b > 0:
            self.canvas.create_rectangle(
                *self.curr_ul, *self.lr,
                tag="remainder", fill="grey")
        self.update_text()
        
    def update_text(self):
        if self.curr_a == 0:
            pgcd = self.curr_b
        elif self.curr_b == 0:
            pgcd = self.curr_a
        else:
            pgcd = "?"
        self.canvas.itemconfigure("text",
              text = f"a = {self.curr_a}, b = {self.curr_b}, pgcd = {pgcd}")


if __name__ == "__main__":
    a, b = argv[1:]
    main = Euclid(a, b)
