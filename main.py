import numpy as np
from gpm import GPM
from Nmatrix import Nmatrix
from Fvector import Fvector
from sympy import Symbol
from sympy import symbols

def main():
    init_x = 0
    gamma = 0

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

    a = GPM(init_x, gamma, f, h, b, num)

    x = [1,2,3]
    # Test Gradient of N
    # b = Nmatrix(h, num).N_calculation(x)
    # print(b)

    # test = a.N()

    # c = Nmatrix(test, num).N_calculation(x)
    # print(c)

    f_test = a.delta_f()
    f_v = Fvector(f,num).f_calculation(x)
    print(f)
    print(f_test)
    print(f_v)
    
    # t = 'x1'
    # a = f.subs(t, 1)
    # b = a.subs(x2, 2)
    # c = b.subs(x3, 3)


if __name__ == '__main__':
    main() 

