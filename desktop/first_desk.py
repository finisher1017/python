from tkinter import *

window = Tk()

window.geometry('500x300+300+400')
window.title('Hello world')
mbutton = Button(text="Jonathan Seubert").grid()
mlabel = Label(text="Welcome", fg = 'grey', bg = 'pink').grid(sticky = W)

window.mainloop()