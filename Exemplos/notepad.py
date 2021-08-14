#! /usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk
from tkFileDialog import asksaveasfilename,askopenfilename


#Começa a classe do editor:
class PyNotePad:
    # Aqui fica a função inicial:
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title("PyNotePad")# Aqui é o Titulo

        # "inicia" a scroolbar
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side='right', fill='y')

        menubar = tk.Menu(self.root)
        #Aqui criamos os menus:
        MENUarquivo = tk.Menu(menubar)
        MENUarquivo.add_command(label="Salvar", command=self.salvar)
        MENUarquivo.add_command(label="Abrir", command=self.abrir)
        menubar.add_cascade(label="Arquivo", menu=MENUarquivo)

        MENUajuda = tk.Menu(menubar)
        MENUajuda.add_command(label="Sobre", command=self.sobre)
        menubar.add_cascade(label="Ajuda", menu=MENUajuda)
        self.root.config(menu=menubar)

        # Aqui adicionamos a parte que fica o texto:
        self.text = tk.Text(self.root, background='DarkMagenta',
                            font=('monospace', 11, 'normal'), foreground='yellow')
        self.text.pack(expand='yes', fill='both')

        #aqui configura o scrollbar
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)


        # Por Fim, a janela:
        self.root.mainloop()

    def salvar(self): # Aqui é a função que salva o arquivo:

        fileName = asksaveasfilename()
        try:
            file = open(fileName, 'w')
            textoutput = self.text.get(0.0, 'end')
            file.write(textoutput)
        except:
            pass
        finally:
            file.close()

    def abrir(self):# Aqui é a função que abre um arquivo
      

        fileName = askopenfilename()
        try:
            file = open(fileName, 'r')
            contents = file.read()

            self.text.delete(0.0, 'end')
            self.text.insert(0.0, contents)
        except:
            pass

    def sobre(self):# uma pequena função "sobre" :D
        root = tk.Tk()
        root.wm_title("Sobre")
        texto=("PyNotePad: Versão 1.0")
        textONlabel = tk.Label(root, text=texto)
        textONlabel.pack()

# inicia o programa:
PyNotePad()
