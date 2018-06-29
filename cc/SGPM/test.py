import numpy as np
from sympy import Symbol
from sympy import symbols
from operations import df
from operations import cf
from operations import mask
from operations import special
from operations import norm
from operations import update
from operations import gf

init_x = [1,2,3]
gamma = 0.2

x1 = Symbol("x1")
x2 = Symbol("x2")
x3 = Symbol("x3")
    
f = [[x1**3 + x2**2 + x3]]
h = [[x1**2+x2**2+x3**2],
    [2*x1**2+x2**2+x3**2],
    [x1**2+4*x2**2+x3**2],
    [x1**3+x2**2+3*x3**2]]
b = [9, 11, 10, 13]
num = 3

# test gf
g = gf(f=h, b=b)
print(h)
print(g)

# test update
# h_ = update(M=h, index=[1,2])
# print(h_)
# h_x = cf(f=h_,num=num, x=[1,2,3])
# print(h_x)

# test operation df, cf
# a = df(f=f, num=num)
# b = df(f=h, num=num)
# print(a,b)
# c = cf(f=a, num=num, x=init_x)
# d = cf(f=b, num=num, x=init_x)
# print(c,d)

matrix = np.asarray([[1,2,3],[4,5,6]])



# (matrix, vector_v, vector_h) = mask(matrix)
# print(vector_h)
# print(vector_v)
# print(matrix)

# O_kx = np.matmul(matrix, np.transpose(matrix))\
#             + np.matmul(np.matmul(matrix,np.transpose(vector_h)),np.transpose(vector_v))\
#             + np.matmul(vector_v, np.matmul(vector_h, np.transpose(matrix)))\
#             + np.matmul(np.matmul(np.matmul(vector_v, vector_h),np.transpose(vector_h)),np.transpose(vector_v))
# print(O_kx)

# a = np.asarray([[0,1,3,2],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
# print(a)
# (o,d) = special(a)
# print(o)
# print(d)

# a = np.random.uniform(-1,1,[3,3])
# print(a)
# b = np.random.uniform(-1,1,[3,3])
# print(b)
# c = norm(a,b)
# print(c)
# def hi(x):
#     i = x
#     while(1):
#         if i == 10:
#             print('OK!OK!OK!')
#             return
#         else:
#             print('NOT OK!')
#             i = i + 1
# hi(3)

[[ -2.87309824e+08],[ -1.34217728e+08],[ -8.05306368e+08]]