'''
Created on 2.11.2017

@author: m1k1e
'''
from Tkinter import *

def Hello(event):
    print ("Hello, User")

root=Tk()

#first comment

btn = Button(root,                  
             text="Click me",       
             width=30,height=5,     
             bg="white",fg="black") 
btn.bind("<Button-1>", Hello)       
btn.pack()                     

root.mainloop()