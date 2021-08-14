# -*- coding: utf-8 -*-
#Nome: Calculadora1.py
#Autor: Arthur Costa Marcondes
#Data : 22/02/2021
# Esse software eh exclusivamente para fins didaticos
# 


import Tkinter as tk
import time

class Matematica():
    def __init__(self):
	self.root=tk.Tk()
	self.root.title("Frações")
	self.root.geometry("500x500+400+40")
	self.root.configure(bg="grey")
	
	self.num1 = 0
	self.num2 = 0
	
	self.ed1 = tk.Entry(self.root)
	self.ed1.place(x=150, y=60)	 
	self.ed2 = tk.Entry(self.root)
	self.ed2.place(x=150, y=30)
	
	self.can = tk.Canvas(self.root, width=480, height=100)
	self.can.place(x=10, y=165)
	
	self.bt1 = tk.Button(self.root, text="Fração", width=4, bg="grey", fg="white", height=1, command = self.bt_click)
	self.bt1.place(x=196, y=100)
	
	self.lb = tk.Label(self.root, text="Resultado")
	self.lb.configure(bg="grey", fg="white")
	self.lb.place(x=193, y=140)
	
	self.vermelho = "red"
	self.azul = "lightBlue"
	
	 
	
	self.root.mainloop()
    
    def bt_click(self):
	self.can.delete("all")
	self.num1 = self.ed1.get()
	self.num2 = self.ed2.get()
	c = 50
	
	try:
	    self.resultado = int(self.num1)-int(self.num2)
	    numerador = float(self.num2)
	    denominador = float(self.num1)
	    self.lb["text"] = str(numerador/denominador)
	    for r in range(int(self.num2)):
		self.a = self.can.create_rectangle(0, 0, 20, 20, fill=self.vermelho)
		self.can.move(self.a, c, 20)
		c = c+20
	    for r in range(self.resultado):
		self.a = self.can.create_rectangle(0, 0, 20, 20, fill=self.azul)
		self.can.move(self.a, c, 20)
		c = c+20
	    
	    
	except:
	    self.lb["text"] = "Erro"
	    self.lb.configure(bg="grey", fg="white")
	    self.lb.place(x=208, y=140)	    
            
	    
	

	
Matematica()
