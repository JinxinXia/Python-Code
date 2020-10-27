# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:47:24 2020

@author: Jinxin
"""

import multiprocessing as mp
import numpy as np
import random 
from time import time

random.seed(50)
# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0,10,size=[2000,5])
data = arr.tolist()
data[:5]


# Solution Without Paralleization
def howmany_within_range(row,minimum,maximum):
    """ Returns how many numbers lie within 'maximum' and 'minimum' in a given 
    'row' """
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

results = []
for row in data:
    results.append(howmany_within_range(row,minimum = 4, maximum = 8))
    
print(results[:10])



# Parallelizing using Pool.apply()

# Step 1: Init multiprocessing.Pool()
pool = mp.Pool(mp.cpu_count())

# Step 2: 'pool.apply' the 'howmany_within_range()'

results1 = []
results1 = [pool.apply(howmany_within_range,args=(row,4,8)) for row in data]

# Step 3: Close
pool.close()

print(results1[:10])



# Parallelizing using Pool.map

# Redefine, with only 1 mandatory argument 
def howmany_within_range_rowonly(row, minimum=4,maximum=8):
    count = 0 
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

pool = mp.Pool(mp.cpu_count())
results2 = []
results2 = pool.map(howmany_within_range_rowonly,[row for row in data])
pool.close()
print(results2[:10])



# Parallelizing with Pool.starmap()
pool = mp.Pool(mp.cpu_count())
results3 = []
results3 = pool.starmap(howmany_within_range,[(row,4,8) for row in data])
pool.close()


# Parallelizing processing with Pool.apply_async()
pool = mp.Pool(mp.cpu_count())

# Step 1: Redefine to accept 'i' the iteration number
def howmany_within_range2(i,row,minimum,maximum):
    """Returns how many numbers lie within 'maximum' and 'minimum' in a given 
    'row' """
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return (i,count)

# Step 2: Define callback function to collect the output in 'results'
def collect_result(result):
    global results4
    results4.append(result)
    
# Step 3: Use loop to parallelize
for i, row in enumerate(data):
    pool.apply_async(howmany_within_range2,args=(i,row,4,8),callback=collect_result)
    
# Step 4: Close Pool and let all the process complete
pool.close()
pool.join() # postpones the excition of next line of code untill all processes in the queue are done.

# Step 5: Sort results
results4.sort(key=lambda x: x[0])
results4_final = [r for i, r in results]

print(results4_final[:10])


# Parallel processing with Pool.apply_async() without callback function
pool = mp.Pool(mp.cpu_count())

results5 = []

# call apply_async() without callback
result_objects = [pool.apply_async(howmany_within_range2,args=(i,row,4,8)) for i, row in enumerate(data)]

# result_objects is a list of pool.ApplyResult objects
results = [r.get()[1] for r in result_objects]

pool.close()
pool.join()
print(results[:10])


# Parallelizing with Poool.starmap_async()

pool = mp.Pool(mp.cpu_count())

results6 = []

results6 = pool.starmap_async(howmany_within_range2,[(i,row,4,8) for i, row in enumerate(data)]).get()

pool.close()
print(results6[:10])
