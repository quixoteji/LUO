import numpy as np
import algebra
import timeit

vNUM = 1000
gNUM = 4000
THRESHOLD = 0.1
gamma = 0.1
ITERATION = 1000
init_x = np.random.rand(vNUM)

def gpm(vNUM, gNUM, THRESHOLD, gamma, init_x, ITERATION):
    k = 0
    x = init_x
    f = algebra.fun_f(vNUM)
    g = algebra.Group_g(vNUM, gNUM)
    N = g.derivative()
    init_x = -1*np.ones(vNUM)
    N_k = N

    # print(f.a,f.b,f.c)
    # for i in g.group:
    #     print(i.a,i.b,i.c)
    while True:
        print('ROUND:', k)
        # 3 
        
        f_k = f.calculate(x)
        # print(x)
        # print(f_k)
        delta_f_k = f.derivative(x)
        # 4
        N1 = np.dot(N_k, N_k.T)
        N2 = np.linalg.inv(N1)
        N3 = np.dot(N_k.T, N2)
        N4 = np.dot(N3, N_k)
        I = np.eye(len(N4))
        P_k = I - N4
        # 5 
        s_k = -1*np.dot(P_k, delta_f_k)
        # print('s1',s_k)
        # 6
        s_value = sum(np.absolute(s_k))
        if s_value >= THRESHOLD:
            print('B1')
            # 7 
            a_k_upper = gamma * f_k
            # print('s2',s_k)
            a_k_below = np.inner(s_k, delta_f_k)
            a_k = -1 * a_k_upper/a_k_below

            g_k = g.calculate(x)

            x1 = a_k * s_k
            x2 = np.inner(N3, g_k)
            x = x + x1 - x2
        else:
            print('B2')
            lambda_k = np.dot(np.dot(N2,N_k),delta_f_k)
            lambda_min = min(lambda_k)
            index = lambda_k.tolist().index(min(lambda_k))
            if lambda_min >= 0: 
                print('B3')
                break
            else:
                print('B4')
                g.group.pop(index)
                N_k = g.derivative()
                x = x
        k = k+1
        if sum(np.absolute(x)) > 1e+10: x = np.random.rand(vNUM)
        if k == ITERATION: break
    # print('f_k', f_k)
    # print('x_k', x)
    return x

start = timeit.default_timer()

gpm(vNUM, gNUM, THRESHOLD, gamma, init_x, ITERATION)

stop = timeit.default_timer()

print(start-stop)