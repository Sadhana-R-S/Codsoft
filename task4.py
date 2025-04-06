import tkinter as tk
import random
def compgen():
    global comp
    choices=["Rock","Paper","Scissor"]
    comp=random.choice(choices)
    compin.config(text="Computer:"+comp)
    whowins()
def rock():
    global user
    user="Rock"
    userin.config(text="You:"+user)
    compgen()
def paper():
    global user
    user="Paper"
    userin.config(text="You:"+user)
    compgen()
def scissor():
    global user
    user="Scissor"
    userin.config(text="You:"+user)
    compgen()
def whowins():
    if (user == "Rock" and comp == "Scissor") or (user == "Scissor" and comp == "Paper") or (user == "Paper" and comp == "Rock"):
            userwin()
           
    elif (user == "Rock" and comp == "Paper") or (user == "Scissor" and comp == "Rock") or (user == "Paper" and comp == "Scissor"):
            compwin()
        
    else:
        draw()
def compwin():
    cwin=tk.Label(root,bg='green',fg='yellow',text="You Lose",font=("Comic Sans MS",50),width=20,height=1)
    cwin.place(x=90,y=30)
    des(cwin)
def userwin():
    uwin=tk.Label(root,bg='orange',fg='green',text="YOU WIN", font=("Comic Sans MS",50),width=20,height=1)
    uwin.place(x=90,y=30)
    des(uwin)
def draw():
    dr=tk.Label(root,bg="blue",fg="orange",text="Draw",font=("Comic Sans MS",50),width=20,height=1)
    dr.place(x=90,y=30)
    des(dr)
def des(t):
    t.after(1000,t.destroy)
root=tk.Tk()
root.config(bg='red')
root.geometry("1000x1000")
frame=tk.Frame(root,bg='pink')
frame.place(x=50,y=20,width=900,height=900)
rockb=tk.Button(root,width=8,height=2,text="ROCK",font=("Impact",30),bg="aqua",command=rock)
paperb=tk.Button(root,width=8,height=2,text="PAPER",font=("Impact",30),bg="aqua",command=paper)
scissorb=tk.Button(root,width=8,height=2,text="SCISSOR",font=("Impact",30),bg="aqua",command=scissor)
rockb.place(x=100,y=200)
paperb.place(x=400,y=200)
scissorb.place(x=700,y=200)
userin=tk.Label(frame,bg="fuchsia",fg="navy",text="",width=20,height=2,font=("CurlzMT",40))
userin.place(x=100,y=350)
compin=tk.Label(frame,bg="purple",fg="gray",text="",width=20,height=2,font=("CurlzMT",40))
compin.place(x=100,y=500)
root.mainloop()
