from tkinter import *

canvas_width = 400
canvas_height =400

master = Tk()

canvas = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
canvas.pack()

img = PhotoImage(file="tut_interface_1.gif")
canvas.create_image(5,5, anchor=NW, image=img)

mainloop()
