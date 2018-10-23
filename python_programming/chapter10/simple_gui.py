import tkinter

#create the root window
root = tkinter.Tk()
root.title("Labeler")
root.geometry("200x100")

#create a frame in the window to hold other widgets
app = tkinter.Frame(root)
app.grid()

#create a label in the frame
lbl = tkinter.Label(app, text = "I'm a label!")
lbl.grid()

#kick off the window's event loop
root.mainloop()