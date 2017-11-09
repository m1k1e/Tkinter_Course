'''
Created on 2.11.2017

@author: m1k1e
'''


from Tkinter import * 


def Hello(event):
    label1.config(text='Hello, user!')


root=Tk()


root.title('First GUI program')


root.geometry("300x200")

label1 = Label(root, bg="red", fg="black", font="20")
label1.place(relx=.5, rely=.3, anchor="c", height=30, width=130, bordermode=OUTSIDE)

btn = Button(root,                  
             text="Click me",       
             width=10,
             height=3,     
             bg="white",
             fg="black",              
             font="12"       
             ) 


btn.bind("<Button-1>", Hello)       
btn.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)                  

root.mainloop() 