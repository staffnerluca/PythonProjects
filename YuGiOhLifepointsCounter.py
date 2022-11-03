import tkinter as tk

window = tk.Tk()
points1 = 8000
points2 = 8000

def configureRowsAndColums():
    window.grid_columnconfigure(0, minsize=250)
    window.grid_rowconfigure(0, minsize=400)
    window.grid_columnconfigure(3, minsize = 150)

def calculate():
    global points1, points2
    if plus1.get() != "":
        points1+=int(plus1.get())
        showPoints1["text"] = points1
    if plus2.get() != "":
        points2+=int(plus2.get())
        showPoints2["text"] = points2
    if minus1.get() != "":
        points1-=int(minus1.get())
        showPoints1["text"] = points1
    if minus2.get() != "":
        points2-=int(minus2.get())
        showPoints2["text"] = points2

if __name__ == "__main__":
    points1 = 8000
    points2 = 8000
    window.configure(bg="purple")
    window.geometry("1000x1000")
    window.maxsize(1000, 1000)
    showPoints1 = tk.Label(window, font=("times", 50), foreground="white", bg="black", text=points1)
    showPoints1.grid(column=2, row = 2) 
    showPoints2 = tk.Label(window, font=("times", 50), foreground="white", bg="black", text=points2)
    showPoints2.grid(column = 4, row = 2)
    plus1 = tk.Entry(window, bg="green")
    minus1 = tk.Entry(window, bg="red")
    plus1.grid(column = 2, row = 3)
    plus2 = tk.Entry(window, bg="green")
    plus2.grid(column = 4, row = 3)
    minus1.grid(column = 2, row = 4)
    minus2 = tk.Entry(window, bg="red")
    minus2.grid(column = 4, row = 4)
    calc = tk.Button(window, text="Calculate", command=calculate)
    calc.grid(column = 3, row = 3)
    configureRowsAndColums()
    window.mainloop()
