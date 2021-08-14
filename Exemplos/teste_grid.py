#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk

class Calculadora:
   def __init__(self, parent):
      self.nValorAtual = 0
      top = self.top = parent
      display = tk.Text(top, height=1, width=20)
      display.tag_config('justified', justify='right')
      display.insert('insert', self.nValorAtual, 'justified')

      btn1 = tk.Button(top, text="1", command=self.p1)
      btn2 = tk.Button(top, text="2", command=self.p2)
      btn3 = tk.Button(top, text="3", command=self.p3)
      btn4 = tk.Button(top, text="4", command=self.p4)
      btn5 = tk.Button(top, text="5", command=self.p5)
      btn6 = tk.Button(top, text="6", command=self.p6)
      btn7 = tk.Button(top, text="7", command=self.p1)
      btn8 = tk.Button(top, text="8", command=self.p8)
      btn9 = tk.Button(top, text="1", command=self.p9)
      btn0 = tk.Button(top, text="0", command=self.p0)

      
      btnC = tk.Button(top, text="C", command=self.pC)
      btnX = tk.Button(top, text="x", command=self.pX)
      btnD = tk.Button(top, text="/", command=self.pD)
      btnS = tk.Button(top, text="-", command=self.pS)
      btnM = tk.Button(top, text="+", command=self.pM)
      btnI = tk.Button(top, text="=", command=self.pI)
      btnP = tk.Button(top, text=".", command=self.pP)

      btn1.grid(row=1, column=0, padx=1, pady=10)
      btn2.grid(row=1, column=1, padx=1, pady=10)
      btn3.grid(row=1, column=2, padx=1, pady=10)
      btn4.grid(row=2, column=0, padx=1, pady=10)
      btn5.grid(row=2, column=1, padx=1, pady=10)
      btn6.grid(row=2, column=2, padx=1, pady=10)
      btn7.grid(row=3, column=0, padx=1, pady=10)
      btn8.grid(row=3, column=1, padx=1, pady=10)
      btn9.grid(row=3, column=2, padx=1, pady=10)
      btn0.grid(row=4, column=1, padx=1, pady=10)

      btnC.grid(row=4, column=0, padx=1, pady=10)
      btnX.grid(row=2, column=3, padx=5, pady=10)
      btnD.grid(row=1, column=3, padx=5, pady=10)
      btnI.grid(row=5, column=3, padx=5, pady=10)
      btnS.grid(row=4, column=3, padx=5, pady=10)
      btnP.grid(row=4, column=2, padx=1, pady=10)
      btnM.grid(row=3, column=3, padx=5, pady=10)

      display.grid(row=0, column=0, columnspan=4)

   def p1(self):
      pass

   def p2(self):
      pass

   def p3(self):
      pass

   def p4(self):
      pass

   def p5(self):
      pass

   def p6(self):
      pass

   def p7(self):
      pass

   def p8(self):
      pass

   def p9(self):
      pass

   def p0(self):
      pass

   def pC(self):
      pass

   def pX(self):
      pass

   def pD(self):
      pass

   def pI(self):
      pass

   def pS(self):
      pass

   def pP(self):
      pass

   def pM(self):
      pass


root = tk.Tk()
Calculadora(root)
root.mainloop()
