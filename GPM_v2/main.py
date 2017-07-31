from sympy import Symbol
from gpm import GPM
import numpy as np
from generate import generate_b
from generate import generate_f
from generate import generate_h
import datetime 

print('Prepare')
print(datetime.datetime.now())
num = 10
init_x = [1 for i in range(num)]
gamma = 0.02
f = generate_f(num)
h = generate_h(num)
b = generate_b(num)

# x1 = Symbol("x1")
# x2 = Symbol("x2")
# x3 = Symbol("x3")
    
# f = [[x1**3 + x2**2 + x3]]
# h = [[x1**2+x2**2+x3**2],
#     [2*x1**2+x2**2+x3**2],
#     [x1**2+4*x2**2+x3**2],
#     [x1**3+x2**2+3*x3**2]]
# b = [9, 11, 10, 13]


def main():
    print('begin')
    print(datetime.datetime.now())
    instance_gpm = GPM(init_x=init_x, \
    gamma=gamma, h=h, f=f, \
    num=num, b=b)
    (x, fx) = instance_gpm.loop()
    print(x)
    print(fx)
    print(datetime.datetime.now())

if __name__ == '__main__':
    main()