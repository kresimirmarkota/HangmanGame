import tkinter as tk 
from tkinter import ttk
from tkinter import Canvas

root = tk.Tk()

def formingUi (root):
    
    Label_word=ttk.Label(frm, text="_ _ _ _ _").grid(column=0, row=0)
    Btn_try=ttk.Button(frm, text="Try", command=root.destroy).grid(column=1, row=1)
    Entry_insert_word = ttk.Entry(frm).grid(column=0,row=1)
   
    
def drawBottomGallow():
    # donji dio stupa
    canvas.create_line(110,150,120,190, fill="black", width=3)
    canvas.create_line(110,150,100,190, fill="black", width=3)
    canvas.create_line(110,80,110,150, fill="black", width=3)

def drawUpperGallow():
    # gornji dio stupa
    canvas.create_line(110,5,110,120, fill="black", width=3)

def drawGallow():
    # vješalo
    canvas.create_line(110,5,160,5, fill="black", width=3)
    canvas.create_line(160,5,160,30, fill="black", width=3)

def drawHead():
    # glava
    canvas.create_oval(140, 30, 180, 70, outline = "black", fill = "white",width = 3)
def drawBody():
    # tijelo
    canvas.create_line(160,60,160,120, fill="black", width=3)

def drawArms():
    # ruke
    canvas.create_line(160,85,170,115, fill="black", width=3)
    canvas.create_line(160,85,150,115, fill="black", width=3)
def drawLegs():
    # noge
    canvas.create_line(160,115,170,145, fill="black", width=3)
    canvas.create_line(160,115,150,145, fill="black", width=3)

frm = ttk.Frame(root,padding=20)
formForDrawing=ttk.Frame(root,padding=10)
frm.grid()
formForDrawing.grid()
formingUi(root)
canvas = Canvas(formForDrawing)


drawBottomGallow()
drawUpperGallow()
drawGallow()
drawHead()
drawBody()
drawArms()
drawLegs()





canvas.grid(column=1, row=0)
root.mainloop()



