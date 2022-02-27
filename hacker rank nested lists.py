# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 07:25:23 2022

@author: sriharsha

Input Format

The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.


"""

n = int(input())
l1 = []
add =0
#print(sli)
for i in range(n):
    sli = list(input().split())
    l1.append(sli)
query_nme = input()
for j in range(n):
    if query_nme == l1[j][0]:
        add =l1[j][1]+l1[j][2]+l1[j][3]
        avg = add/3
print("%.2f"%avg)
    