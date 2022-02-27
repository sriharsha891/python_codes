# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 08:36:46 2021

@author: sriharsha
"""

import numpy as np
import pandas as pd
import random 
"Creating a data set of employee and salary"
employee = ["Employee"+ str(i) for i in range(1,1001)]

"""list of all the employes by name"""
employe1 = pd.Series(employee)

sal = [10000,20000,35000,65000,22000,90000]
"""genrating random salaries using random module"""
salar = np.random.choice(a=sal,size = 1000)
Salary = pd.Series(salar)

"""generating years of experience for each employee"""
#years = np.random.randint(1,10)
years = [1,2,3,4,5,6,7,8,9,10]
exp = np.random.choice(a=years,size = 1000)
exp1 = pd.Series(exp)

"""generating degree for each employee"""
degree = ["B.Tech","BBA","MBA","M.Tech","10thpass","Inter"]
deg = np.random.choice(a=degree,size = 1000)
degree1 = pd.Series(deg)

"""generating expenditure of the employee"""
sal2 = [1000,2000,3500,6500,2200,9000]
expenses = np.random.choice(a=sal2,size = 1000)
expenditure = pd.Series(expenses)

"""creating a dictionary"""
df = {"Employ_list":employe1,
      "Salary":Salary,
      "Years_of_experience":exp1,
      "Degree":degree1,
      "Expenditure":expenditure}

DF = (pd.DataFrame(df))
#DF.to_excel("employ_list_update2.xlsx")
print(DF)

file = [DF.Salary.describe(),
DF.Years_of_experience.describe(),
DF.Degree.describe(),
DF.Degree.value_counts()]
new_file = pd.DataFrame(file)
new_file.to_excel("new_file.xlsx")










