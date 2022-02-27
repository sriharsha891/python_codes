# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:46:16 2022

@author: sriharsha
"""

n = int(input("Enter year: "))
def leap(year):
   return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
if leap(n)==True:
    print("it's leap year")
else:
    print("it's not a leap year")
