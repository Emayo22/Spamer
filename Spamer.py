import pyautogui
from time import sleep
from tkinter import *


def clicked():
    text = txt.get()
    message = txt2.get()
    if message == "":
        message = "0"
    message = int(message)
    pyautogui.click(0, 2)
    while message > 0:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
        message -= 1


window = Tk()
window.configure(background='#3D3D3D')
window.title("Spamer")
window.geometry('400x250')
window.iconbitmap('hack.ico')

lbl = Label(window, text="Text of messages", bg = "#3D3D3D", fg="white")
lbl.grid(column=0, row=0)

lb2 = Label(window, text="Number of messages ", bg = "#3D3D3D", fg="white")
lb2.grid(column=0, row=1)

txt = Entry(window,width=10, bg = "#5A5853", fg = "white")
txt.grid(column=1, row=0)

txt2 = Entry(window,width=10, bg = "#5A5853", fg = "white")
txt2.grid(column=1, row=1)

btn = Button(window, text="Start", command = clicked, bg = "#3D3D3D", fg = "white")
btn.grid(column=2, row=1)

window.mainloop()
