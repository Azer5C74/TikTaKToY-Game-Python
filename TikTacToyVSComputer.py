import timeit
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
import time
#Global variables
ActivePlayer=1

p1_list=[] #what player 1 selected
p2_list=[] #what player 2 selected
root=Tk()
root.title("Tic Tac Toy :Player 1")
style=ttk.Style()
style.theme_use('classic')

#Add Buttons
but1=ttk.Button(root,text=' ') #create button
but1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40) #use of grid() to arrange widget in rows and collumns
but1.config(command=lambda: ButtonClick(1))


but2=ttk.Button(root,text=' ') #create button
but2.grid(row=0,column=1,sticky='snew',ipadx=40) #use of grid() to arrange widget in rows and collumns
but2.config(command=lambda: ButtonClick(2))


but3=ttk.Button(root,text=' ') #create button
but3.grid(row=0,column=2,sticky='snew',ipadx=40) #use of grid() to arrange widget in rows and collumns
but3.config(command=lambda: ButtonClick(3))


but4=ttk.Button(root,text=' ') #create button
but4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40) #use of grid() to arrange widget in rows and collumns
but4.config(command=lambda: ButtonClick(4))

but5=ttk.Button(root,text=' ') #create button
but5.grid(row=1,column=1,sticky='snew',ipadx=40) #use of grid() to arrange widget in rows and collumns
but5.config(command=lambda: ButtonClick(5))

but6=ttk.Button(root,text=' ') #create button
but6.grid(row=1,column=2,sticky='snew',ipadx=40) #use of grid() to arrange widget in rows and collumns
but6.config(command=lambda: ButtonClick(6))


but7=ttk.Button(root,text=' ') #create button
but7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40) #use of grid() to arrange widget in rows and collumns
but7.config(command=lambda: ButtonClick(7))


but8=ttk.Button(root,text=' ') #create button
but8.grid(row=2,column=1,sticky='snew',ipadx=40) #use of grid() to arrange widget in rows and collumns
but8.config(command=lambda: ButtonClick(8))

but9=ttk.Button(root,text=' ') #create button
but9.grid(row=2,column=2,sticky='snew',ipadx=40) #use of grid() to arrange widget in rows and collumns
but9.config(command=lambda: ButtonClick(9))


def ButtonClick(id): #specifying action after click
    global ActivePlayer

    if(ActivePlayer==1):
        SetLayout(id,"X")
        p1_list.append(id)
        root.title("Tic Tac Toy :Player 2")
        ActivePlayer=2
        print("P1_list:{}".format(p1_list))
        AutoPlay()

    else:
        SetLayout(id,'O')
        p2_list.append(id)
        root.title("Tic Tac Toy :Player 1")
        ActivePlayer=1
        print("P2_list:{}".format(p2_list))
    CheckWinner()
    #CheckDraw()

def SetLayout(id,PlayerSymbol):
    if(id==1):
        but1.config(text=PlayerSymbol)
        but1.state(["disabled"])
    elif id==2:
        but2.config(text=PlayerSymbol)
        but2.state(["disabled"])
    elif id==3:
        but3.config(text=PlayerSymbol)
        but3.state(["disabled"])
    elif id==4:
        but4.config(text=PlayerSymbol)
        but4.state(["disabled"])
    elif id==5:
        but5.config(text=PlayerSymbol)
        but5.state(["disabled"])
    elif id==6:
        but6.config(text=PlayerSymbol)
        but6.state(["disabled"])
    elif id==7:
        but7.config(text=PlayerSymbol)
        but7.state(["disabled"])
    elif id==8:
        but8.config(text=PlayerSymbol)
        but8.state(["disabled"])
    else:
        but9.config(text=PlayerSymbol)
        but9.state(["disabled"])

def CheckWinner():
    global winner
    winner=-1
    if ((1 in p1_list) and (2 in p1_list) and (3 in p1_list)):
        winner=1
    if ((1 in p2_list) and (2 in p2_list) and (3 in p2_list)):
        winner=2

    if ((4 in p1_list) and (5 in p1_list) and (6 in p1_list)):
        winner = 1
    if ((4 in p2_list) and (5 in p2_list) and (6 in p2_list)):
        winner = 2

    if ((7 in p1_list) and (8 in p1_list) and (9 in p1_list)):
        winner = 1
    if ((7 in p2_list) and (8 in p2_list) and (9 in p2_list)):
        winner = 2

    if ((1 in p1_list) and (4 in p1_list) and (7 in p1_list)):
        winner = 1
    if ((1 in p2_list) and (4 in p2_list) and (7 in p2_list)):
        winner = 2

    if ((2 in p1_list) and (5 in p1_list) and (8 in p1_list)):
        winner = 1
    if ((2 in p2_list) and (5 in p2_list) and (8 in p2_list)):
        winner = 2

    if ((3 in p1_list) and (6 in p1_list) and (9 in p1_list)):
        winner = 1
    if ((3 in p2_list) and (6 in p2_list) and (9 in p2_list)):
        winner = 2

    if ((7 in p1_list) and (5 in p1_list) and (3 in p1_list)):
        winner = 1
    if ((7 in p2_list) and (5 in p2_list) and (3 in p2_list)):
        winner = 2

    if ((9 in p1_list) and (5 in p1_list) and (1 in p1_list)):
        winner = 1
    if ((9 in p2_list) and (5 in p2_list) and (1 in p2_list)):
        winner = 2


    if(winner==1):
        messagebox.showinfo(title="Congrats !!!",message="Player 1 is the winner")
        time.sleep(1)
        exit()

    elif(winner==2):
        messagebox.showinfo(title="Congrats !!!",message="Player 2 is the winner")
        time.sleep(2)
        exit()
    if(len(EmptyCells)==0):
        messagebox.showinfo(title="DRAW !!!",message="NO ONE WON !!!")
        time.sleep(1)
        exit()

def AutoPlay():
    global EmptyCells
    EmptyCells=[]

    RandIndex = 0

    for cell in range(9):
        if(not((cell+1 in p1_list)or (cell+1 in p2_list))):
            EmptyCells.append(cell+1)
    print(EmptyCells)
    if(len(p1_list)<2):
        if(5 in EmptyCells):
            ButtonClick(5)
        else:
            RandIndex=randint(0,len(EmptyCells)-1)
            ButtonClick(EmptyCells[RandIndex])
    else:
        x=p1_list[len(p1_list)-1]
        y=p1_list[len(p1_list)-2]

        print(len(p1_list))
        print(len(p2_list))
        ButtonClick(EmptyCells[randint(0,len(EmptyCells)-1)])
root.mainloop()
