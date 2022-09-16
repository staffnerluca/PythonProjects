import tkinter
from tkinter import ttk
from tkinter import filedialog
import plotly
import plotly.express as pex
import pandas
import random

window = tkinter.Tk()

def boxplot(data, xText="x", yText="y", color="black"):
    boxplot=pex.box(data, color_discrete_sequence=["purple"])
    boxplot.show()

def histogram(data, xText="x", yText="y", color="black"):
    pass

def bulkdiagramm(data, xText="x", yText="y", color="black"):
    pass

def lineDiagramm(data, xText="x", yText="y", color="black"):
    lineDia=pex.line(data, x=xText, y=yText, color_discrete_sequence=[color])
    lineDia.show()

#executes all functions needed to visualise the data
def visualise():
    fileName = filedialog.askopenfilename()
    #define colors
    #get text from text boxes
    x = txtX.get() 
    print(x)
    #TODO function to get data from excel or database
    data = pandas.read_excel(fileName, header=0,  engine="openpyxl")
    ##data=[]
    #for i in range(200):
        #data.append(random.randint(0, 100))
    boxplot(data)
    histogram(data)
    bulkdiagramm(data)
    #lineDiagramm(data)
    #logLineDiagramm(data)

if __name__ == "__main__":
    window.configure(bg="black")
    #design
    window.geometry("900x500")
    window.maxsize(900, 500)
    window.grid_rowconfigure(3, minsize=200)
    start=tkinter.Button(window, command=visualise, text="choose dataset")
    start.grid(column=3, row=4)

    #creats the and places the buttons, lables and so forth.    
    window.grid_columnconfigure(0, minsize=100)
    window.grid_columnconfigure(2, minsize=100)
    window.grid_columnconfigure(4, minsize=100)
    lblX=tkinter.Label(window, font=("Times", 15), foreground="white", bg="black", text="Text for the x-axis")
    lblX.grid(column=1, row=0)
    txtX=tkinter.Entry(window, bg="white")
    txtX.grid(column=1, row=1)
    
    lblY=tkinter.Label(window, font=("Times", 15), foreground="white", bg="black", text="Text for the y-axis")
    lblY.grid(column=3, row=0)
    txtY=tkinter.Entry(window, bg="white")
    txtY.grid(column=3, row=1)

    lblColor=tkinter.Label(window, font=("Times", 15), foreground="white", bg="black", text="choose color scheme")
    lblColor.grid(column=5, row=0)
    cBoxColor=ttk.Combobox(window, values=["b/w", "rainbow", "red", "purple", "blue", "green"], background="white")
    cBoxColor.grid(column=5, row=1)

    window.mainloop()
