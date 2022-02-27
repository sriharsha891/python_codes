# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 08:36:46 2021

@author: sriharsha
"""
"""step 1 univariet analysis of concrete data """
import numpy as np
import pandas as pd
import seaborn as sns
"""reading the given file"""
f1 = pd.read_csv('C:/Users/sriharsha/Desktop/concrete.csv')

"""finding the datatypes"""
print(f1.dtypes)
print(f1.describe())
print(f1.mean())
print(f1.std())
print(f1.strength.max())
"""outliers detection using box plot"""
ott = sns.boxplot(x = f1["cement"])
ott1 = sns.boxplot(x = f1["strength"])
#slag,water,superplastic,fineagg,age,strength
"""the above mentioned columns have
 outliers which we found out using boxplot in univariet analysis"""

"""Here we analysed Uni-variate outlier i.e. 
we used each column only to check the outlier. But we can do multivariate outlier analysis too.
 Can we do the multivariate analysis with Box plot? Well it depends,
 if you have a categorical values then you can use that with any 
 continuous variable and do multivariate outlier analysis. 
 As we do not have categorical value in our concrete dataset, 
 we might need to forget about using box plot for multivariate outlier 
 analysis"""
"""finding the null values"""
print(f1[["slag"]].value_counts())
print(pd.Series(dir(f1)))
print(dir(f1))


