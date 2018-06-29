import numpy as np
import algebra

vNUM = 1000
gNUM = 4000
THRESHOLD = 0.1
gamma = 0.1
ITERATION = 1000
init_x = np.random.rand(vNUM)

def clinet():
    k = 0
    x = init_x
    f = algebra.fun_f(vNUM)
    g = algebra.Group_g(vNUM, gNUM)
    N = g.derivative()
    init_x = -1*np.ones(vNUM)
    N_k = N

    while True:
        print('ROUND', k)


