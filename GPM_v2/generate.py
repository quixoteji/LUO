import numpy as np
from sympy import diff
from sympy import evalf
from math import sqrt
from sympy import Symbol

def generate_f(num):
    x_symbols = []
    for i in range(1, num+1):
        s = 'x' + str(i)
        s = Symbol(s)
        x_symbols.append(s)
    power3 = np.random.randint(low=0, high=100, size=[1,num])[0].tolist()
    power2 = np.random.randint(low=0, high=100, size=[1,num])[0].tolist()
    power1 = np.random.randint(low=0, high=100, size=[1,num])[0].tolist()
    s = 0
    for i in range(num):
        s = s + power3[i] * x_symbols[i]**3
    for i in range(num):
        s = s + power2[i] * x_symbols[i]**2
    for i in range(num):    
        s = s + power1[i] * x_symbols[i]
    return [[s]]


def generate_h(num):
    x_symbols = []
    for i in range(1, num+1):
        s = 'x' + str(i)
        s = Symbol(s)
        x_symbols.append(s)
    h = [[0] for i in range(num)]
    for i in range(num):
        xpower = np.random.randint(low=0, high=100, size=[1,num])[0].tolist()
        ypower = np.random.randint(low=0, high=100, size=[1,num])[0].tolist()
        xs = 0
        ys = 0
        for j in range(num):
            xs = xs + xpower[j] * x_symbols[j]
            ys = ys + ypower[j] * x_symbols[j]
        hs = xs * ys
        h[i][0] = hs.expand(basic=True)
    return h

def generate_b(num):
    seed = np.random.randint(low=0, high=100, size=[1,num])[0]
    return seed.tolist()