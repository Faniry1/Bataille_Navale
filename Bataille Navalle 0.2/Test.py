from tkinter import *

root = Tk()
cnv = Canvas()

def quitter():
    root.destroy()
    
btn1 = Button(text ="Quit",command=quitter)

btn1.place(x=70,y=60,anchor=SE)
cnv.place()

root.mainloop()