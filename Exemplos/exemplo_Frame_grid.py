#! /usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		#Listbox.__init__(self)
		#self.grid()
		#self.master.title("Grid Manager")
	
		for r in range(8): #6
			self.master.rowconfigure(r, weight=1)    
		for c in range(6): #5
			self.master.columnconfigure(c, weight=1)
			Button(master, activebackground="green", bg="lightblue", fg= "red", text="Button {0}".format(c)).grid(row=8,column=c,sticky=E+W)
			
		#Button[0].configure(bg="red")
	
		Frame1 = Frame(master, bg="red")
		self.grades(1,2,Frame1)
		Frame1.grid(row = 0, column = 0, rowspan=5, columnspan=2, pady=3, padx=2, sticky = W+E+N+S) #red
		
		self.editor = Listbox(Frame1,fg="red",bg="black")
		scrollbar1 = Scrollbar(Frame1,orient="vertical")
		self.editor.config(yscrollcommand=scrollbar1.set)
		scrollbar1.config(command=self.editor.yview)
		self.editor.grid(row=0,column=0,columnspan=2, padx=2, pady=2,sticky= W+E+N+S)
		scrollbar1.grid(row=0,column=2, sticky= N+S)
		
		Frame2 = Frame(master, bg="blue")
		self.grades(2,3,Frame2)
		Frame2.grid(row = 5, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)# blue
		
		self.terminal = Listbox(Frame2, bg="orange", fg="yellow")
		scrollbar2 = Scrollbar(Frame2,orient="vertical")
		self.terminal.config(yscrollcommand=scrollbar2.set)
		scrollbar2.config(command=self.terminal.yview)
		self.terminal.grid(row=0,column=0,columnspan=3, rowspan=2, padx=2, pady=2,sticky= W+E+N+S)
		scrollbar2.grid(row=0,column=3, rowspan=2, sticky= N+S)
		
		self.comandG = Entry(Frame2, bg="darkmagenta",fg="yellow")
		self.comandG.grid(row=2,column=0,columnspan=3, padx=2, pady=2,sticky= W+E)  
		
		Frame3 = Frame(master, bg="green")
		self.grades(3,3,Frame3)
		Frame3.grid(row = 0, column = 2, rowspan = 8, columnspan = 4, padx=3, pady=3, sticky = W+E+N+S)# green
		self.canvas = Canvas(Frame3, bg="LightGreen")
		hbar=Scrollbar(Frame3,orient='horizontal')
		vbar=Scrollbar(Frame3,orient='vertical')
		hbar.config(command=self.canvas.xview)
		vbar.config(command=self.canvas.yview)
		self.canvas.config(xscrollcommand=hbar.set)
		self.canvas.config(yscrollcommand=vbar.set)
		self.canvas.grid(row=0, column=0, columnspan=3, rowspan=3, padx=2, pady=2,sticky= W+E+N+S)
		hbar.grid(row=3,column=0, columnspan=3, sticky="wens")
		vbar.grid(row=0,column=3, rowspan= 3, sticky="wens")
		
	def grades(self, linha, coluna, tela):
		for r in range(linha): tela.rowconfigure(r, weight=1)
		for c in range(coluna): tela.columnconfigure(c, weight=1)
			
		
root = Tk()
root.geometry("400x200+200+200")
app = Application(master=root)
app.mainloop()
