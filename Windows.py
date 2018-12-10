from tkinter import *
from tkinter import ttk 
root=Tk()
def SOST(*args):
    post.set(pre.get())
    pre.set(" ")

root.title("Sostituzione")
mainframe=ttk.Frame(root)
mainframe.grid(column=0,row=0)

pre=StringVar()
post=StringVar()

ttk.Label(mainframe,textvariable=post).grid(column=0,row=0)

ttk.Entry(mainframe,width=7, textvariable=pre).grid(column=0,row=1)

ttk.Button(mainframe,text="Converti").grid(column=1,row=2)

root.mainloop()     