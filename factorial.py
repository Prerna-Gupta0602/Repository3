# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:48:00 2020

@author: DELL
"""

print("It is a program to compute the factorial of a number input by the user")

n = int(input("Enter the number : "))

def fact(n):
    if n < 0:
        return f"please enter a positive number"
    if not isinstance(n, int):
        return f"please enter an integer"
    else:
        if n == 1:
            return 1
        else:
            return n * fact(n-1)
        
print("factorial of",n, "is", fact(n))

