from tkinter import *

a = Tk()
a.geometry("400x400")
a.title("Calculator")
a.configure(bg="#1e1e1e")   # Window background color

# Entry Box
x = Entry(
    a,
    width=20,
    font="Arial 20",
    bg="#2d2d2d",
    fg="white",
    bd=5,
    justify="right"
)
x.grid(row=0, column=0, columnspan=4, pady=10)

# Functions
def click(num):
    current = x.get()
    x.delete(0, END)
    x.insert(0, str(current) + str(num))

def clear():
    x.delete(0, END)

def equal():
    try:
        res = eval(x.get())
        x.delete(0, END)
        x.insert(0, res)
    except:
        x.delete(0, END)
        x.insert(0, "Error")

# Button Colors
num_bg = "#4d4d4d"
op_bg = "#ff9500"
clear_bg = "#ff3b30"
equal_bg = "#34c759"

# Row 1
Button(a, text="1", width=5, height=2, font="Arial 20",
       bg=num_bg, fg="white",
       command=lambda: click(1)).grid(row=1, column=0, padx=5, pady=5)

Button(a, text="2", width=5, height=2, font="Arial 20",
       bg=num_bg, fg="white",
       command=lambda: click(2)).grid(row=1, column=1, padx=5, pady=5)

Button(a, text="3", width=5, height=2, font="Arial 20",
       bg=num_bg, fg="white",
       command=lambda: click(3)).grid(row=1, column=2, padx=5, pady=5)

Button(a, text="+", width=5, height=2, font="Arial 20",
       bg=op_bg, fg="white",
       command=lambda: click("+")).grid(row=1, column=3, padx=5, pady=5)

# Row 2
Button(a, text="4", width=5, height=2, font="Arial 20",
       bg=num_bg, fg="white",
       command=lambda: click(4)).grid(row=2, column=0, padx=5, pady=5)

Button(a, text="5", width=5, height=2, font="Arial 20",
       bg=num_bg, fg="white",
       command=lambda: click(5)).grid(row=2, column=1, padx=5, pady=5)

Button(a, text="6", width=5, height=2, font="Arial 20",
       bg=num_bg, fg="white",
       command=lambda: click(6)).grid(row=2, column=2, padx=5, pady=5)

Button(a, text="-", width=5, height=2, font="Arial 20",
       bg=op_bg, fg="white",
       command=lambda: click("-")).grid(row=2, column=3, padx=5, pady=5)

# Row 3
Button(a, text="7", width=5, height=2, font="Arial 20",
       bg=num_bg, fg="white",
       command=lambda: click(7)).grid(row=3, column=0, padx=5, pady=5)

Button(a, text="8", width=5, height=2, font="Arial 20",
       bg=num_bg, fg="white",
       command=lambda: click(8)).grid(row=3, column=1, padx=5, pady=5)

Button(a, text="9", width=5, height=2, font="Arial 20",
       bg=num_bg, fg="white",
       command=lambda: click(9)).grid(row=3, column=2, padx=5, pady=5)

Button(a, text="*", width=5, height=2, font="Arial 20",
       bg=op_bg, fg="white",
       command=lambda: click("*")).grid(row=3, column=3, padx=5, pady=5)

# Row 4
Button(a, text="C", width=5, height=2, font="Arial 20",
       bg=clear_bg, fg="white",
       command=clear).grid(row=4, column=0, padx=5, pady=5)

Button(a, text="0", width=5, height=2, font="Arial 20",
       bg=num_bg, fg="white",
       command=lambda: click(0)).grid(row=4, column=1, padx=5, pady=5)

Button(a, text="=", width=5, height=2, font="Arial 20",
       bg=equal_bg, fg="white",
       command=equal).grid(row=4, column=2, padx=5, pady=5)

Button(a, text="/", width=5, height=2, font="Arial 20",
       bg=op_bg, fg="white",
       command=lambda: click("/")).grid(row=4, column=3, padx=5, pady=5)

a.mainloop()