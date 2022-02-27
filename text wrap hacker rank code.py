# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 07:29:19 2022

@author: sriharsha

Text wrap
"""
# =============================================================================
# string = input()
# width = int(input())
# li = []
# 
# for i in string:
#     li.append(i)
# li.reverse()
# r = (len(li)//width)
# 
# for k in range(1+r):
#     ne = ""
#     for j in range(width):
#         if li !=[]:
#           ne += li.pop(-1)
#     print(ne,end = '\n')
# =============================================================================
  
  
import textwrap
def wrap(string,max_width):
    """hacker rank text wrap code"""  
    li = []
    for i in string:
        li.append(i)
    li.reverse()
    r = (len(li)//max_width)

    for k in range(r):
        ne = ""
        for j in range(max_width):
            if li !=[]:
              ne += li.pop(-1)
        print(ne,end='\n')
    p= ""
    for i in (li):
        p+=i        
    return p[::-1]
         

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)