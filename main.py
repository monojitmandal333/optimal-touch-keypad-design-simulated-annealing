import ast
import numpy as np
from global_vars import *
import math
import utils


T=50
#Roe value
r=0.85
count=0
n_keys = 27

X = utils.initialize_solution(n_keys)
#Terminating condition 
while T > 0.0001 and count <= 40:
    print(count)
    #Find out fitness value
    old_obj = utils.calculate_objective(
        X = X,
        bp = BIGRAM_PROBABILITY_MATRIX,
        mt = MOVEMENT_TIME_MATRIX
    )
    print(f'Old objective: {old_obj:.4f}')
    X_new = utils.move(X)
    new_obj = utils.calculate_objective(
        X = X,
        bp = BIGRAM_PROBABILITY_MATRIX,
        mt = MOVEMENT_TIME_MATRIX
    )
    #Difference between old and new fitness value
    diff = old_obj - new_obj
    # If difference is zero then we will definitely accept it,otherwise we will have some probability value to accept it
    if diff >= 0:
        if round(diff,3) == 0:
            count+=1
        p = 1
    else:
        count+=1
        p = math.exp(diff/T)
    if utils.is_acceptable(p) == True:
        T = r*T
        X = X_new.copy()
        print(f'New objective: {new_obj:.4f}')
        print(f'Temperature: {T:4f}')

print('The minimum value of objective function: ',old_obj)
print('The assignment matrix is:\n')
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Space']
solution_array=['']*n_keys
for i in range(n_keys):
    for j in range(n_keys):
        if X[i][j] == 1:
            solution_array[i] = alphabet[j]
print(solution_array)