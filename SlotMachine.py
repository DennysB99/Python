#
# CGS 2060 – Spring Semester 2024
#
# CGS 2060 Homework #3 – Creating A Slot Machine
#
# (Dennys Bach)
#

from tkinter import *
import random

global Symbols
#global Icon1,Icon2,Icon3
Symbols = ('♠', '♥', '♣', '♦', 'X', 'Ω')
Total = 0.0

def RunGame():
  Wins = [[],[],[]]
  global Total

  Generate = random.randint(0,5)
  Wins[0]=Symbols[Generate]
  Generate = random.randint(0,5)
  Wins[1]=Symbols[Generate]
  Generate = random.randint(0,5)
  Wins[2]=Symbols[Generate]
  Icon1 ["text"] = Wins[0]
  Icon2 ["text"] = Wins[1]
  Icon3 ["text"] = Wins[2]

  Counting = Wins.count("X")
  if Counting == 1:
      Total+=0.10
  elif Counting == 2:
      Total+=0.25
  elif Counting == 3:
      Total+=0.50
  elif Counting == 0:
      Total+=0
  MoneyDisp ["text"] = "Money Won: $" + str('{0:.2f}').format(Total)

Window = Tk()
Layer = Frame(Window)
Window.geometry("1000x400")
Window.resizable(False,False)
Window.title("Slot Machine")
#Label the game
Game = Label(Window,text="Slot Machine",font=50)
Game.pack()
Layer.pack()
#Set up 3 locations for icons
Icon1 = Button(Layer,text="x",font=50,height=6,width=25)
Icon1.pack(side=LEFT)
Icon2 = Button(Layer,text="x",font=50,height=6,width=25)
Icon2.pack(side=LEFT)
Icon3 = Button(Layer,text="x",font=50,height=6,width=25)
Icon3.pack(side=LEFT)
#Button
SlotButton = Button(Window,text="Press here!",font=25,height=6,width=20,command=RunGame)
SlotButton.pack(side=BOTTOM)
#Money Display
MoneyDisp = Label(Window,text = "Money Won: $",font=50)
MoneyDisp.pack(side=BOTTOM)

Window.mainloop()


