def updateMenu(event):
    label['text'] = str(event) + '\n' + str(Lb.curselection())
    print(label['text'])

# import all functions from the tkinter  
from tkinter import *
import tkinter

m = tkinter.Tk()
m.title('Menu')
""" select_btn = tkinter.Button(m, text='elegir', width=25, command=m.destroy)
select_btn.pack() """
#top = Tk()
label= tkinter.Label(m)
Lb = Listbox(m)
Lb.insert(1, 'Omelette de jamón y queso')
Lb.insert(2, 'Revuelto Gramajo')
Lb.insert(3, 'Albóndigas')
Lb.insert(4, 'Ensalada completa')
Lb.pack()
Lb.bind('<<ListboxSelect>>', updateMenu)
# create a Submit Button and place into the root window
# when user press the button, the command or
# function affiliated to that button is executed
#Submit = Button(m, text = "Submit", fg = "Black", bg = "Red", command = updateMenu)
m.mainloop()

