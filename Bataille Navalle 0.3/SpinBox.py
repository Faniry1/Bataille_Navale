from tkinter import *


# root window
root = Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Spinbox Demo')

# Spinbox
current_value = StringVar(value=0)
spin_box = Spinbox(
    root,
    from_=0,
    to=30,
    textvariable=current_value,
    wrap=True)

spin_box.pack()

root.mainloop()