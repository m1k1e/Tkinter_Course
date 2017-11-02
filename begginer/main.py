'''
Created on 2 лист. 2017 р.

@author: m1k1e
'''
from Tkinter import *

def Hello(event):
    print "Hello, User!"

root=Tk()

btn = Button(root,                  #родительское окно
             text="Click me",       #надпись на кнопке
             width=30,height=5,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
btn.pack()                     

root.mainloop()