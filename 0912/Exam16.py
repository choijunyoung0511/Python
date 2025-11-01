from tkinter import*
from tkinter import messagebox

def clickRight(event) :
    messagebox.showinfo("마우스","마우스 오른쪽 버튼이 클릭됨")


window = Tk()

window.bind("<Button-3>",clickRight())

window.mainloop()
