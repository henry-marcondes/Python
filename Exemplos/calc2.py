#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arthur Costa Marcondes
# email: arthur.marcondes@educaiguape.com.br
# git: htpps://github.com/arthur-marcondes/Programas
# Date: 08/03/2021
#----------------------------------------------------
# Este programa pode ser compartilhado respeitando
# os Direitos de não modificar o autor.
#----------------------------------------------------


import Tkinter as tk

class Fatias:
	def __init__(self,parent):
		raiz = self.raiz = parent
		self.raiz.title("Polignos")
		self.raiz.geometry("500x300+400+40")
		self.coords = 10,10,150,150
		self.canvas=tk.Canvas(raiz, width=400, height=250)
		self.canvas.pack()
		self.frame=tk.Frame(raiz)
		self.frame.pack()
		self.canvas.create_oval(self.coords,fill='deepskyblue', outline='darkblue')
		fonte=('Comic Sans MS', '14', 'bold')
		tk.Label(self.frame, text='Fatia: ',
					font=fonte, fg='blue').pack(side="left")
		self.porcentagem=tk.Entry(self.frame, fg='red',font=fonte, width=5)
		self.porcentagem.focus_force()
		self.porcentagem.pack(side="left")
		tk.Label(self.frame, text='%',font=fonte, fg='blue').pack(side="left")
		self.botao=tk.Button(self.frame, text='Desenhar',
							command=self.cortar, font=fonte,
							fg='darkblue', bg='deepskyblue')
		self.botao.pack(side="left")
		tk.Label(self.frame, text="Angulo", font=fonte).pack(side="left")
		self.lb1 = tk.Label(self.frame, text="",font=fonte)
		self.lb1.pack(side="left")
		
	def cortar(self):
		arco=self.canvas.create_arc
		#fatia=float(self.porcentagem.get())*359.9/100.
		fatia=int(self.porcentagem.get())
		inicio = 0.0
		passo = 360.0/float(fatia)
		texto= str(passo)
		self.lb1["text"] = "%d graus"%passo
		for a in range(fatia):
			arco(self.coords,start=inicio,extent=passo, fill="yellow")
			inicio=inicio+passo
			  
		new_coords = 140,140,280,280
		arco(new_coords, extent=passo, fill='LightGreen', outline='red')
		self.porcentagem.focus_force()
		
instancia=tk.Tk()
Fatias(instancia)
instancia.mainloop()
		
		
		
