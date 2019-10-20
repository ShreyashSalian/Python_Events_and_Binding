from tkinter import *
s = Tk()
def key_pressed(event):
    print("Key Pressed",repr(event.char))

def callback(event):
    f.focus_set()
    print("Clicked At",event.x,event.y)

f = Frame(s,width=100,height=100)
f.bind("<Key>",key_pressed)
f.bind("<Button-1>",callback)
f.pack()
s.mainloop()
