#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arthur Costa Marcondes
# email: arthur.marcondes@educaiguape.com.br
# git: htpps://github.com/arthur-marcondes/Programas
# Date: 17/03/2021
#----------------------------------------------------
# Este programa pode ser compartilhado respeitando
# os Direitos de não modificar o autor.
#----------------------------------------------------

# incluir a opção de comparar os multiplos#
# executado por Henry               
# incluir ajuda para uso do programa 

import Tkinter as tk

class Mult_1:
	def __init__(self, parent):
		raiz = self.raiz = parent
		self.raiz.geometry("500x400+100+100")
		self.raiz.configure(bg="red")
		self.c = []
		self.d = {}
		
		for r in range (2):
		    self.raiz.rowconfigure(r, weight=1)
		for c in range (1):
		    self.raiz.columnconfigure(c, weight=1)  
		      
		self.frame1 = tk.Frame(raiz, bg="LightGreen", height=250)
		self.frame1.grid(row=0, column=0, padx=1, pady=1, sticky="wnes")
		
		self.frame2 = tk.Frame(raiz, bg="LightGreen", height=250)
		self.frame2.grid(row=1, column=0, padx=1, pady=1, sticky="wnes")
		
		msg = "O programa ira calcular uma quantidade X de números \n conforme a formúla abaixo."
		
		lb1 = tk.Label(self.frame1, text=msg, bg="LightGreen", fg="black")
		lb1.grid(row=0, column=0, padx=1, pady=1)
		
		msg = "M(X)={ X*0, X*1, X*2, X*3, X*4, X*N, ... }"
		
		lb2 = tk.Label(self.frame1, text=msg, bg="LightGreen", fg="red")
		lb2.grid(row=1, column=0, padx=1, pady=1)
		
		msg = "Defina o valor de X:"
		lb3 = tk.Label(self.frame1, text=msg, bg="LightGreen", fg="black")
		lb3.grid(row=2, column=0, padx=1, pady=1)
		
		self.ed1 = tk.Entry(self.frame1, width=5)
		self.ed1.grid(row=2, column=1, padx=1, pady=1)
		
		
		msg = "Defina o valor de N:"
		
		lb4 = tk.Label(self.frame1, text=msg, bg="LightGreen", fg="black")
		lb4.grid(row=3, column=0, padx=1, pady=1)
		
		self.ed2 = tk.Entry(self.frame1, width=5)
		self.ed2.grid(row=3, column=1, padx=1, pady=1)
		
		
		msg = "Calcular"
		botao = tk.Button(self.frame1, text=msg, command=self.formula)
		botao.grid(row=4, column=1, padx=1, pady=1)
		
		msg = "Limpar Calculos"
		botao1 = tk.Button(self.frame1, text=msg, command=self.limpar)
		botao1.grid(row=4, column=0, padx=1, pady=1)
		
		msg = "Multiplo Comum"
		botao2 = tk.Button(self.frame1, text=msg, command=self.multiplos)
		botao2.grid(row=5, column=0, padx=1, pady=1)
		
		self.ed3 = tk.Entry(self.frame1, width=5)
		self.ed3.grid(row=5, column=1, padx=1, pady=1)
		
		self.ed4 = tk.Entry(self.frame1, width=5)
		self.ed4.grid(row=5, column=2, padx=1, pady=1)
		
		self.scrollbar = tk.Scrollbar(self.frame2, orient="horizontal")
		
		for r in range (2):
		    self.frame2.rowconfigure(r, weight=1)
		for c in range (1):
		    self.frame2.columnconfigure(c, weight=1)
		
		self.txt1 = tk.Listbox(self.frame2, bg="magenta", width=62, xscrollcommand=self.scrollbar.set)
		self.txt1.grid(row=0, column=0, rowspan=2, padx=1, pady=1, sticky="wnes")
		
		self.scrollbar.config(command=self.txt1.xview)
		self.scrollbar.grid(row=2, column=0, columnspan=2, sticky="we")
	
	def formula(self):
		r = []
		X = int(self.ed1.get())
		N = int(self.ed2.get())	
		for i in range(N):
			s = i*X
			r.append(s)

		self.d.update({X:r})	    
		msg= "M(%d) = %s" %(X,r)
		self.txt1.insert("end", msg)
	
	def limpar(self):
		self.txt1.delete(0,tk.END)
		
	def multiplos(self):
		a = int(self.ed3.get())
		b = int(self.ed4.get())
		self.compara(a,b)
	
	def compara(self, a, b):
		try:
			self.a = self.d.get(a)
			self.b = self.d.get(b)
			self.c = []
			for i in self.a:
				for j in self.b:
					if i == j:
						self.c.append(j)
			msg = "M(%d,%d) = %s "%(a,b,self.c)
			self.txt1.insert("end",msg)
		except:
			msg = "Dados Incorretos"
			self.txt1.insert("end",msg)
		
    
	
instancia =tk.Tk()
Mult_1(instancia)
instancia.mainloop()
