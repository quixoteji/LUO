import numpy as np
import sympy 
from Nmatrix import Nmatrix
from Fvector import Fvector
from M_operation import M_operation

"""
Generate constrains for the nonlinear function
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
        # Polynomial vector for delta f
        self.delta_f = Fvector(f,num).delta_f_generation()
        # Polymonial matrix for N 
        self.N = Nmatrix(h,b,num).N_generation()
        self.g = Nmatrix(h,b,num).g_generation()

    def loop(self):
        x_k = self.init_x
        gamma = self.gamma
        N = self.N
        g = self.g
        f = self.f
        times = 0
        while 1:
            # *_k: the value of polynomial 
            print(times)
            N_k = np.asarray(M_operation(self.num).calculate(N, x_k),dtype=np.float32)    # 3
            delta_f_k = np.asarray(M_operation(self.num).calculate(self.delta_f, x_k),dtype=np.float32) # 3 
            I = np.eye(len(np.transpose(N_k)))
            # M = (N*NT)-1
            # test1 = np.transpose(N_k)
            # test2 = np.matmul(N_k,test1)
            # M = np.linalg.inv(test2)
            M = np.linalg.inv(np.matmul(N_k,np.transpose(N_k)))
            # test1 = np.transpose(N_k)
            # test2 = np.matmul(test1,M)
            # test3 = np.matmul(test2, N_k)
            # P_k = I - test3
            P_k = I - np.matmul(np.matmul(np.transpose(N_k),M), N_k) # 4
            s_k = -np.matmul(delta_f_k, P_k) # 5
            # print(self.decision(s_k))
            if self.decision(s_k):
                lambda_k = np.matmul(np.matmul(M,N_k),delta_f_k) #7
                lambda_min = min(lambda_k)        #7
                index = np.where(lambda_k == lambda_min)
                index = np.ndarray.tolist(index[0])
                if lambda_min >= 0:
                    f_k = M_operation(self.num).calculate(self.f, x_k)              #8
                    return (x_k, f_k) #9
                else:
                    N = M_operation(self.num).update(N, index)
                    g = M_operation(self.num).update(g, index)  # 11 12
            else:   # 13
                medium = np.matmul(np.transpose(s_k), delta_f_k)
                print(f)
                f_k = M_operation(self.num).calculate(f, x_k)
                print(f_k)
                alpha_k = -gamma*f_k/medium
                g_k = M_operation(self.num).calculate(g, x_k)
                x_k = x_k + alpha_k * s_k - np.matmul(np.matmul(np.transpose(N_k),M),g_k)
            times = times + 1

    # Decide whether the vector is all zeros
    # True is all zeros
    def decision(self, s):
        zeros = np.zeros_like(s)
        # print('1')
        # print(s.size)
        # print('2')
        # print(zeros == s)
        # print('3')
        # print(sum(sum(zeros==s)))
        # print('4')
        # print(sum(zeros == s) == s.size)
        return (sum(sum(zeros == s)) == s.size)
