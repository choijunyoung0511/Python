from tkinter import *
from tkinter import messagebox

def myFunc() :
    messagebox.showinfo("버튼","유영상은 부자다 ?^^")

window = Tk()

photo = PhotoImage(file ="../GIF/dog2.gif")
button1 = Button(window, image= photo, command= myFunc)

button1.pack()
window.mainloop()