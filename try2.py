import tkinter as tk
import random
import string
def value():
    l=plen.get()
    check(l)
def check(l):
    try:
        l=int(l)
        if l>1:
            global num
            num=l
            passgen(num)
        else:
            raise ValueError
    except ValueError:
        err=tk.Label(root,text="Enter a Valid Number",font=("Georgia",20),bg="blue",fg="white")
        err.after(1000,err.destroy)
        err.pack()
def passgen(num):
    pw=""
    for i in range(0,num):
        allc="ABCEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890,!@#$%^&*()<>.?/+|={}[]:;"
        pw+=random.choice(allc)
    res.config(text=pw)
root=tk.Tk()
root.geometry("500x500")
root.config(bg='pink')
frame=tk.Frame(root,bg='purple')
frame.pack(padx=30,pady=30)
digno=tk.Label(root,width=17,height=1,text="Password Length",font=("Georgia",30),fg="blue",bg="aqua")
digno.place(x=50,y=100)
digno.pack()
plen=tk.Entry(root,width=17,font=("Georgia",20),fg="brown")
plen.pack()
ent=tk.Button(root,text="Enter",font=("Georgia",15),command=value)
ent.pack()
sugp=tk.Label(root,text="Suggested Password",width=17,height=1,font=("Georgia",30),fg="yellow",bg="green")
sugp.pack()
res=tk.Label(root,text="",width=17,height=1,font=("Georgia",30),fg="olive")
res.pack()
root.mainloop()
