# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:53:59 2019

@author: hr
"""

import Tkinter as tk
import dic as d
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Tradutor:
    def __init__(self, parent):
        top = self.top = parent
        fonte1 = ("Verdana", "11", "bold")
        titulo1 = tk.Label(top, text='ING:', fg='blue', font=fonte1)
        titulo1.grid(row=0, column=0, padx=1, pady=1)
        
        self.palavra = tk.Entry(top, font=fonte1, width=30)
        self.palavra.focus_force()
        self.palavra.grid(row=0, column=1, padx=1, pady=1)
        
        bt1 = tk.Button(top, text='TRAD', font=fonte1)
        bt1.bind("<Return>", self.traducao)
        bt1.grid(row=0, column=4, padx=1, pady=1)
        
        bt2 = tk.Button(top, text='NEW', font=fonte1)
        bt2.bind("w", self.Nova)
        bt2.grid(row=0, column=5, padx=1, pady=1)
        
        titulo2 = tk.Label(top, text='IN:', fg='green', font=fonte1)
        titulo2.grid(row=1, column=0,padx=1,pady=1)
        self.ingles = tk.Label(top, font=fonte1, text='  ',fg='blue', justify='left')
        self.ingles.grid(row=1, columnspan=5,padx=1, pady=1)
        titulo3 = tk.Label(top, text='PT:', font=fonte1, fg='black')
        titulo3.grid(row=2, column=0, padx=1, pady=1)
        self.trad = tk.Message(top, font=fonte1,fg='red', justify='left',
                          width=400,text='ING -> TAB -> TR para NEW e w ')
        self.trad.grid(row=2, column=1, padx=1, pady=1)



    def Nova(self, event):
        palavra = self.ingles['text']
        self.trad['text']='Nova Palavra Inclusa!'
        nova = self.palavra.get()
        incluindo = 'dic'+"['"+ palavra +"']='"+ nova +"'\n"
	print palavra + " = "+ nova
        
        f = open('dic.py', 'a')
        f.write( incluindo)
        f.close()
        self.palavra.focus_force()
        self.palavra.delete(0, 'end')
        
        
    def traducao(self, event):
        
        t = self.palavra.get()
        try:
            s = d.dic[t]
            self.ingles['text'] = t
            self.trad['text'] = s
            
        except KeyError:
            self.ingles['text'] = t
            self.trad['text'] = 'Insira a tradução: New -> W '
            
        self.palavra.delete(0,'end')
        self.palavra.focus_force()
        
        
instancia =tk.Tk()
Tradutor(instancia)
instancia.mainloop()
            
