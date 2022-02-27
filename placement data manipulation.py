# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:25:57 2022

@author: sriharsha
"""

import pandas as pd
df = pd.read_csv("C:/Users/sriharsha/Documents/Placement_Data_Full_Class.csv")
df.head()
df.info()
df.shape
df.describe()

temp_status = df.loc[:,"status"]
temp_status

temp_spec_hr = (df.loc[(df.specialisation == "Mkt&HR"),'specialisation'])
temp_spec_hr

placed = df.loc[df.status == "Placed",'status']
placed


salary = df.loc[(df.salary>0),'salary']
salary

spec_hr = df.loc[(df.specialisation == 'Mkt&Fin')]
spec_hr

spec_fin = df.loc[df.specialisation == "Mkt&Fin",'specialisation']
spec_fin
new_df = pd.DataFrame({"status":placed,
                       "hr_specialisation":temp_spec_hr,
                       "salary":salary
    })

new_df
mkt_hr= new_df.dropna()
mkt_hr
print(mkt_hr)
