
# Project 

logo = '''
 ________  ___  ___  _______   ________   ________           _________  ___  ___  _______           ________   ___  ___  _____ ______   ________  _______   ________     
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\___   ___\\  \|\  \|\  ___ \         |\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \|___ \  \_\ \  \\\  \ \   __/|        \ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \            \ \  \ \ \   __  \ \  \_|/__       \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \            \ \  \ \ \  \ \  \ \  \_|\ \       \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \            \ \__\ \ \__\ \__\ \_______\       \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|\_________\\_________\            \|__|  \|__|\|__|\|_______|        \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|
                                 \|_________\|_________|                                                                                                                 
                                                                                                                                                                         
                                                                                                                                                                         
'''
print(logo)
from random import randrange
number = int(randrange(0,100))
print("Welcome to Guss the Number Game")
a = int(input("Please enter the mode of game: \n 1-Easy \n 2-Hard \n \n "))
c= 0
if a==1:
    c = 10
else:
    c = 6
d = False
while c>0:
    b = int(input("Please Choose a Number \n"))
    def check():
        global b
        global number
        global c
        global d
        if b>number:
            print("Too High")
        elif b<number:
            print("Too Low")
        elif b == number:
            print(f"\n You Won the game the number was {number}")
            c = 1 
            d = True
    check()
    c -= 1
    if c>0:
        print(f" \n You have {c} more gusses left \n")
if d == False:
    print("\n You Lost")