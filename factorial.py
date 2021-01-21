# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:48:00 2020

@author: DELL
"""

"""program to compute the factorial of a number"""

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
        
print(fact(n))

