from tkinter import *
from datetime import *

window1 = Tk()
window1.title('Application')
window1.geometry('600x400')

entry = Entry()
label = Label(text = "Hello!", fg ="#000080", bg = "#008080", height = 1, width = 600)
namelabel = Label(text = "Please enter your name", fg = "White", bg = "Black", height = 1, width = 200)
textbox = Text(height = 3, width = 200)

def Displaymssg():
    name = entry.get()
    mssg = "Welcome to my application \n Todays date is: "
    greetingmssg = "Hello"+ name +"\n"
    textbox.insert(END, greetingmssg)
    textbox.insert(END, mssg)
    textbox.insert(END, date.today())

button = Button(text = "Submit", command = Displaymssg, height= 1, width= 100)

label.pack()
namelabel.pack()
entry.pack()
button.pack()
textbox.pack()
window1.mainloop()
