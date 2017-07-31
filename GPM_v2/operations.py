import numpy as np
from sympy import diff
from sympy import evalf
from math import sqrt

'''
df: Partial differential of the algebra functions
cf: Caculate the value of the functions
'''

def df(num, f):
    '''
    Partial differential of the algebra functions
    '''
    # construct the symbols for all variable
    x_symbols = []
    for i in range(1, num+1):
        s = 'x' + str(i)
        x_symbols.append(s)
    
    # construct the Jacobian matrix(zero matrix first) 
    (r,c) = (len(f),num)
    df = [[0 for i in range(c)] for j in range(r)]
    # assign Jacobian matrix
    r_counter = 0
    for i in f:
        for c_counter in range(c):
            diff_ = diff(i[0], x_symbols[c_counter])
            df[r_counter][c_counter] = diff_
        r_counter = r_counter + 1
    r_counter = 0
    return df

def cf(num, f, x):
    '''
    Calculate the value of the function
    '''
    # make sure dimension of vector x is equal to the num of variables in f
    if len(x)==num:
        # reconstruct the size and shape of f
        (r,c) = (len(f), len(f[0]))
        # reconstruct all the symbols in f
        x_symbols = []
        for i in range(1, num+1):
            s = 'x' + str(i)
            x_symbols.append(s)
        # construct dictionary for symbols and their values
        subs_duct = {}
        for i in range(num):
            subs_duct[x_symbols[i]] = x[i]
        # reconsturct matrix f with all zeros
        cf = [[0 for x in range(c)] for j in range(r)]
        # substitute all values into the matrix
        for i in range(r):
            for j in range(c):
                value = f[i][j].evalf(subs=subs_duct)
                cf[i][j] = value
        # return numpy darray
        cf = np.asarray(cf, dtype=np.float32)
        return cf
    else:
        print("Something wrong with the dimension in calculation")
        return

def gf(f, b):
    '''
    Generate g(x)
    '''
    # construct the Jacobian matrix(zero matrix first) 
    l = 0
    (r,c) = (len(f), len(f[0]))
    f_ = [[0 for i in range(c)] for j in range(r)]
    for i in f:
        f_[l][0] = i[0] - b[l]
        l = l + 1
    return f_


def mask(matrix):
    '''
    Add mask to the matrix
    vector_h: horizontal dimension vector
    vector_v: vertical dimension vecotor
    '''
    v, h = len(matrix), len(matrix[0])
    # vector_v = np.transpose(np.ones(v)[np.newaxis])
    vector_v = np.ones([v,1])
    # print(vector_v, vector_v.shape)
    vector_h = np.ones([1,h])
    # print(vector_h, vector_h.shape)
    matrix = np.dot(vector_v, vector_h)
    return (matrix, vector_v, vector_h)

def special(O):
    '''
    O_r = remain part of O
    d_matrix = diagonal matrix of )_r
    '''
    # Extract diagonal of matrix O_r
    d = np.diag(O)
    d_r = np.diag(d)
    O_r = O - d_r
    d = d.tolist()
    for i in range(len(d)):
        if d[i] == 0:
            d[i] = 1
    d_matrix = np.diag(np.asarray(d))
    return (O_r, d_matrix)

def norm(A, B):
    result_matrix = (A-B)**2
    result_array = result_matrix.reshape(1, A.size)
    result_value = sum(result_array.tolist()[0])
    result = sqrt(result_value)
    return result_value

def decision(s):
    '''
    Terminate constrains
    '''
    s1 = s**2
    s2 = sum(s1[0].tolist())
    s3 = sqrt(s2)
    print('S:',s3)
    if s3 < 10:
        return True
    else:
        return False

def find_minimum(vector):
    '''
    return minimum is a scala
    index is a list
    '''
    minimum = min(vector)
    index = vector.index(minimum)
    return (minimum, index)

def update(M, index):
    try:
        for i in index:
            M.pop(i)
        return M
    except:
        M.pop(index)
        return M