from tkinter import *


def clicked():
    lbl.configure(text="Button was cliked")

window = Tk()

window.title("Welcome to LikeGeeks app")
window.geometry("350x200")

lbl = Label(window, text="Hello",font=("Arial Bold",12))

lbl.grid(column=0, row=0)

btn = Button(window,text="Click Me",command=clicked)
btn.grid(column=1,row=0)

txt = Entry(window,width=10)
txt.grid(column=2,row=0)

window.mainloop()