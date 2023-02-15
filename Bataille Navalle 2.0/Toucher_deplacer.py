from tkinter import Tk, Canvas

root = Tk()
cnv = Canvas(root, width=300, height=200)
cnv.pack()


def quitter(event):
    cnv.delete()
    x,y = event.x, event.y
    cnv.create_rectangle(x-10,y-10,x+10,y+10)
cnv.bind("<Button-1>",quitter)

root.mainloop()