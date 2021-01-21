# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:39:01 2020

@author: DELL
"""
import random
from termcolor import colored

print("""\nWelcome to Rock-Paper-Scissors game
              
You are named as the User in the game, playing against the Computer

lets assign Rock = 1, Paper = 2, Scissors = 3

Rules of the game are as follows: 
    
Rock loses to Paper
Rock wins over Scissors
Paper loses to Scissors

Let's Play!""")

#sample_space is the list of all the possible outcomes 

global_var = 0    #x is a global variable
sample_space = [1,2,3]

def enter_choice():
    User = int(input(colored("""Enter User's choice as :
1     for    Rock
2     for    Paper
3     for    Scissors \n\n""", 'green')))
    if User not in sample_space:
        print(colored("please enter a valid choice from 1,2 and 3 only", color = 'red', attrs = ['bold']))
        enter_choice()
    else:
        return User

def choice(a):
    if a == 1:
        return 'Rock'
    elif a == 2:
        return 'Paper'
    else:
        return 'Scissors'
    
def take_turns():
    User_input = enter_choice()
    #print('User gave the input as : ', User_input)
    print("User's choice = ", (colored(choice(User_input), 'blue')))
    Comp_input = random.choice(sample_space)
    #print('Computer chose :', Comp_input)
    print("Computers choice = ", (colored(choice(Comp_input), 'blue')))
    global global_var
    global_var = [User_input,Comp_input]
    #print("x = ", x)
    if User_input == Comp_input:
        print(colored("\nBoth the choices can not be the same, please choose again", color = 'red', attrs = ['bold']))
        take_turns()
    else:
    #print("x = ", x)
        return global_var

def ask_again():
    s = input("Do you want to play again, enter Y for Yes or N for No : ")
    if s == 'Y':
        game_result()
    elif s == 'N':
        pass
    else:
        print(colored("please enter Y or N", color = 'red', attrs = ['bold']))
        ask_again()
        
def game_result():
    take_turns()
    #print(x)
    Outcome1 = global_var[0]
    Outcome2 = global_var[1]
    
    if Outcome1 == 1:
        if Outcome2 == 2:
            print(colored("\nComputer wins", color = 'magenta', attrs = ['bold']))
        elif Outcome2 == 3:
            print(colored("\nUser wins", color = 'magenta', attrs = ['bold']))
    elif Outcome1 == 2:
        if Outcome2 == 1:
            print(colored("\nUser wins", color = 'magenta', attrs = ['bold']))
        elif Outcome2 == 3:
            print(colored("\nComputer wins", color = 'magenta', attrs = ['bold']))
    else:
        if Outcome2 == 1:
            print(colored("\nComputer wins", color = 'magenta', attrs = ['bold']))
        elif Outcome2 == 2:
            print(colored("\nUser wins", color = 'magenta', attrs = ['bold']))
    ask_again()
    
game_result()
    
    
    