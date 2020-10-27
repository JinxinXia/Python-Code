# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:27:55 2020

@author: Jinxin
"""

import numpy as np
import pandas as pd
import multiprocessing as mp

df = pd.DataFrame(np.random.randint(3,10,size=[5,2]))
print(df.head())

# Row wise Operation
def hypotenuse(row):
    return round(row[1]**2 + row[2]**2,2)**0.5

with mp.Pool(4) as pool:
    result = pool.imap(hypotenuse,df.itertuples(name=False),chunksize=10)
    output = [round(x,2) for x in result]

print(output)


# Column wise Operation
def sum_of_squares(column):
    return sum([i**2 for i in column[1]])

with mp.Pool(2) as pool:
    result = pool.imap(sum_of_squares,df.iteritems(),chunksize = 10)
    ouput = [x for x in result]
    
print(output)

