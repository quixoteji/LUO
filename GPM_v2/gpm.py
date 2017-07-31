import numpy as np

from sympy import symbols
from sympy import diff
from sympy import evalf
from sympy import Symbol

from operations import df
from operations import cf
from operations import gf
# from operations import mask
from operations import special
from operations import decision
from operations import find_minimum
from operations import update

"""
Gradient Projection Method:
Solve nonlinear objective functions with nonlinear constrains
"""
class GPM(object):
    def __init__(self, init_x, gamma, f, h, b, num):
        '''
        init_x: initial value of x
        gamma:  prefixed value
        f:      minimization function
        h:      constrains functions
        b:      bias for h
        num:    number of variables
        '''
        self.init_x = init_x
        self.gamma = gamma
        self.f = f
        self.h = h
        self.b = b
        self.num = num
        # # Polynomial vector for delta f
        # self.delta_f = Fvector(f,num).delta_f_generation()
        # # Polymonial matrix for N 
        # self.N = Nmatrix(h,b,num).N_generation()
        # self.g = Nmatrix(h,b,num).g_generation()

    def loop(self):
        # initial all functions before iteration
        # initial x_k
        x_k = self.init_x
        gamma = self.gamma
        f = self.f
        num = self.num
        # Generate matrix N, matrix delta_f, matrix g
        N = df(f=self.h, num=num)
        delta_f = df(f=f, num=num)
        g = gf(f=self.h, b=self.b)
        times = 0
        f_k = cf(f=f, num=num,x=x_k)
        print(f_k)
        while 1:
            # display iteration times
            print(times)
            # 3 calculate delta_f_k, N_k
            delta_f_k = cf(f=delta_f, x=x_k, num=num)
            N_k = cf(num=num, f=N, x=x_k)
            # 4 calculate P_k
            (mN, nN) = N_k.shape
            I = np.eye(nN)
            m1 = np.matmul(N_k, np.transpose(N_k))
            m2 = np.matmul(np.linalg.inv(m1), N_k)
            m3 = np.matmul(np.transpose(N_k), m2)
            P_k = I - m3
            # 5 calculate s_k
            s_k = -np.matmul(delta_f_k, P_k)
            # print(s_k, s_k.shape)
            if decision(s_k):
                lambda_k = np.matmul(m2, delta_f_k)
                (lambda_min, index) = find_minimum(lambda_k)
                # 8
                if lambda_min >= 0:
                    # 9 jump to 17 
                    f_k = cf(f=f, x=x_k, num=num)
                    return (x_k, f_k) 
                else:
                    N = update(M=N, index=index)
                    g = update(M=g, index=index)  # 11 12
            else: 
                # 13
                # calculate f(x_k)
                f_k = cf(f=f, num=num, x=x_k) 
                # calculate alpha_k
                t1 = np.dot(s_k, np.transpose(delta_f_k))[0][0]
                t2 = gamma*f_k[0][0]
                alpha_k = -t2/t1
                # 15 find new x_k
                g_k = cf(f=g, num=num,x=x_k)
                # print(g_k, g_k.shape)
                tm = np.matmul(np.transpose(N_k),np.linalg.inv(m1))
                # print(tm, tm.shape)
                x_k_ = np.asarray(x_k, dtype=np.float32).reshape(1,3)
                # print(x_k_, x_k_.shape)
                # print(alpha_k*s_k, (alpha_k*s_k).shape)
                tmm = np.matmul(tm, g_k).reshape(1,3)
                x_k = x_k_ + alpha_k*s_k + tmm
                x_k = x_k[0].tolist()
            times = times + 1
            f_k = cf(f=f, num=num,x=x_k)
            print(x_k)
            print(f_k)
            g_k =cf(f=g, num=num, x=x_k)
            print(g_k)
