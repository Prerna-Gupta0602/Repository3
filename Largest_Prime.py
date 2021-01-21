# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:30:34 2020

@author: DELL
"""

""" find the largest prime factor of a number"""

num = int(input("Enter an integer "))
lst1 = []
for i in range(2, num):
    if num%i == 0:
        lst1.append(i)

set1 = set()
for j in lst1 :
    flag = True
    for k in range(2,j):
        if j%k == 0:
            flag = False
            break
        
    if flag:
        set1.add(j)
    elif j == 2:
        set1.add(j)
        
print("Largest Prime Factor of", num, "is", max(set1))