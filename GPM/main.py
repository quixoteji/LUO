import numpy as np
from gpm import GPM
from Nmatrix import Nmatrix
from Fvector import Fvector
from sympy import Symbol
from sympy import symbols

def main():
    init_x = [1,1,1]
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

    a = GPM(init_x=init_x, gamma=gamma, f=f, h=h, b=b, num=num)

    (x_min, f_min) = a.loop()
    print(x_min, f_min)
  


if __name__ == '__main__':
    main() 

