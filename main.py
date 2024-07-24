#
# CGS 2060 – Spring Semester 2024
#
# CGS 2060 Homework #2 – Let’s Play Bingo!
#
# (Dennys Bach)
#

import random


Generated = 0
global Bingo
#Create Lists
CalledNums = []
CalledNum = 0
UsedCard = []
BRow = []
IRow = []
NRow = []
GRow = []
ORow = []
Bingo = 0

#Loop to generate a called number
def Caller():
  CalledNum = random.randint(1,76)
  if CalledNum not in CalledNums:
    CalledNums.append(CalledNum)
    print("The number is:")
    print()
    print("         , - ~ ~ ~ - ,")
    print("     , '               ' ,")
    print("   ,                       ,")
    print("  ,                         ,")
    print(" ,                           ,")
    print(" ,           ",CalledNum,"            ,")
    print(" ,                           ,")
    print("  ,                         ,")
    print("   ,                       ,")
    print("     ,                  , '")
    print("        ' - , _ _ _ ,  '")
    return CalledNum
  else:
    Caller()

#Loop to check numbers on card
def CardCheck():
  CalledNum = Caller()
  x = 0
  if CalledNum in BRow:
    x = BRow.index(CalledNum)
    BRow.pop(x)
    BRow.insert(x,"x")
    print("You got one!")

  elif CalledNum in IRow:
    x = IRow.index(CalledNum)
    IRow.pop(x)
    IRow.insert(x,"x")
    print("You got one!")
  elif CalledNum in NRow:
    x = NRow.index(CalledNum)
    NRow.pop(x)
    NRow.insert(x,"x")
    print("You got one!")

  elif CalledNum in GRow:
    x = GRow.index(CalledNum)
    GRow.pop(x)
    GRow.insert(x,"x")
    print("You got one!")
  elif CalledNum in ORow:
    x = ORow.index(CalledNum)
    ORow.pop(x)
    ORow.insert(x,"x")
    print("You got one!")

  else:
    print("Let's try again!")

#Loop to Check for Bingo
def BingoCheck():
  Bingo = 0

  BCol = [BRow[0],IRow[0],NRow[0],GRow[0],ORow[0]]
  ICol = [BRow[1],IRow[1],NRow[1],GRow[1],ORow[1]]
  NCol = [BRow[2],IRow[2],NRow[2],GRow[2],ORow[2]]
  GCol = [BRow[3],IRow[3],NRow[3],GRow[3],ORow[3]]
  OCol = [BRow[4],IRow[4],NRow[4],GRow[4],ORow[4]]
  VertL= [BRow[0],IRow[1],NRow[2],GRow[3],ORow[4]]
  VertR= [BRow[4],IRow[3],NRow[2],GRow[1],ORow[0]]

  for Column in range(5):
    if BCol.count("x") == 5:
      Bingo = 1
    elif ICol.count("x") == 5:
      Bingo = 1
    elif NCol.count("x") == 5:
      Bingo = 1
    elif GCol.count("x") == 5:
      Bingo = 1
    elif OCol.count("x") == 5:
      Bingo = 1
    elif VertL.count("x") == 5:
      Bingo = 1
    elif VertR.count("x") == 5:
      Bingo = 1
    elif BRow.count("x") == 5:
      Bingo = 1
    elif IRow.count("x") == 5:
      Bingo = 1
    elif NRow.count("x") == 5:
      Bingo = 1
    elif GRow.count("x") == 5:
      Bingo = 1
    elif ORow.count("x") == 5:
      Bingo = 1

  if Bingo == 1:
    print()
    print("Congratulations you got Bingo!")
    print()
    start()

#Loop to generate Bingo Card
def BingoCard():
  global Card

  while len(BRow) < 5:
    Generated = random.randint(1,76)
    if Generated not in UsedCard:
        BRow.append(Generated)
        UsedCard.append(Generated)

  while len(IRow) < 5:
    Generated = random.randint(1,76)
    if Generated not in UsedCard:
        IRow.append(Generated)
        UsedCard.append(Generated)

  #Adds the Freebie space in the middle of the card
  while len(NRow) < 5:
    if len(NRow) == 2:
        NRow.append("x")
        continue

    Generated = random.randint(1,76)
    if Generated not in UsedCard:
        NRow.append(Generated)
        UsedCard.append(Generated)

  while len(GRow) < 5:
    Generated = random.randint(1,76)
    if Generated not in UsedCard:
        GRow.append(Generated)
        UsedCard.append(Generated)

  while len(ORow) < 5:
    Generated = random.randint(1,76)
    if Generated not in UsedCard:
        ORow.append(Generated)
        UsedCard.append(Generated)

  #Combine Bingo Card
  Card = [BRow,IRow,NRow,GRow,ORow]

#loop for the game
def main():
  print()

  #Call the loop for the called number
  while Bingo != 1:
    print("Your Bingo Card:")
    print(Card[0])
    print(Card[1])
    print(Card[2])
    print(Card[3])
    print(Card[4])
    print()
    #x = input("Press enter to continue:")
    CardCheck()
    #x = input("Press enter to continue:")
    BingoCheck()

#Loop to start game or exit
def start():
  print("Welcome to Bingo!")
  Game = input("Would you like to play? ")
  print("Please note if you receive an error, you lose.")
  if Game.upper() == "Y":
    BingoCard()
    main()

  elif Game.upper() == "N":
    print("Exiting Game!")
    exit

#Game
start()


