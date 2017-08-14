import numpy as np
from math import sqrt

# ***************************
# Generate df, N, g
def df(f):
    '''
    Partial differential of f
    f: 3 part[[],[],[]]
    '''
    # df size: variables
    df = [0 for i in range(len(f[0]))]
    w = [0 for i in range(len(f[0]))]
    for i in range(len(df)):
        ff = f.copy()
        ff.pop(i)
        df[i] = ff
        w[i] = [f[0][i],f[1][i],f[2][i]]
    
    return (df, w)

def cdf(f, x):
    '''
    Calculate df value
    '''        
    
    
def N(h):
    '''
    Partial differential of h
    f: 3 part[[],[],[]]
    '''
    pass    

def g(g):
    return g

# ***************************
# calculate f, g, delta_f, N
def cf(f, x):
    '''
    Calculate the value of the f
    return: 1
    '''
    final = 0
    for i in f:
        result = np.dot(i,x)
        final += result
    return final
    
def cg(g, b, x):
    '''
    calculate the value of the g
    return: (1,num)
    '''
    # number of constrains
    # nc = len(cg)
    final = [0 for i in range(len(g))]
    for i in range(len(g)):
        m = 0
        for j in g[i]:
            result = np.dot(j, x)
            m += result
        final[i] = m - b[i]
    return final



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
    if s3 < 50:
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