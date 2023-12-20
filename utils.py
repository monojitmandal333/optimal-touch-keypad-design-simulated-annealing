import ast
import numpy as np
import random
import math

def read_data_matrix(
    file_path:str
) -> np.array:
    file = open(file_path, "r")
    data = ''
    for line in file.readlines():
        data = data + line
    file.close()
    return np.array(ast.literal_eval(data))

def normalize(data:np.array) -> np.array:
    n = data.shape[0]
    for i in range(n):
        data[i]=data[i]/np.sum(data[i])
    return data

def calculate_objective(
    X:np.array,
    bp:np.array,
    mt:np.array
) -> np.array:
    n = bp.shape[0]
    a=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    a+=mt[i][j]*bp[k][l]*X[k][i]*X[l][j]
    return(a)

def initialize_solution(n):
    return np.identity(n)

# Swap two rows
def move_swap_single(X,i,j):
    a = X[i].copy()
    b = X[j].copy()
    X[i] = b
    X[j] = a
    return X

# Swap first n rows with last n nows
def move_swap_multiple(X,n_rows):
    return np.roll(X,n_rows,axis=0)
 
# def move_3(X,n_rows):
#     n = X.shape[0]
#     index_swapped = list(np.arange(n - n_rows,n)) + list(np.arange(n_rows,n - n_rows)) + list(np.arange(n_rows))
#     X = X[index_swapped,]
#     return X

def move(X):
    n = X.shape[0]
    i=random.randint(1,n)
    j=random.randint(1,math.floor(n/2))
    if i <= 10:
        X = move_swap_single(X,i,j)
    elif 11 <= i <= 21:
        X = move_swap_multiple(X,j)
    elif 22 <= i <= 24:
        X = move_swap_multiple(X,2)
    elif 24 <= i <= 26:
        X = move_swap_multiple(X,5)
    return X

def is_acceptable(p):
    if p == 1:
        return True
    else:
        rand_num = random.random()
        if p >= rand_num:
            return True
        else:
            return False