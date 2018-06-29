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
        x_k = np.asarray(self.init_x, dtype=np.float32)
        print(x_k.shape)
        gamma = self.gamma
        N = self.N
        g = self.g
        f = self.f
        times = 0
        while 1:
            # *_k: the value of polynomial 
            print(times)
            instance_A = M_operation(self.num)
            N_k = np.asarray(instance_A.calculate(N, x_k),dtype=np.float32)    # 3
            instance_B = M_operation(self.num)
            delta_f_k = np.asarray(instance_B.calculate(self.delta_f, x_k),dtype=np.float32) # 3 
            # instance_C is for f
            instance_C = M_operation(self.num)
            # instance_D is for g
            instance_D = M_operation(self.num)
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
                print(s_k.shape, delta_f_k.shape)
                # medium = np.matmul(np.transpose(s_k), delta_f_k)
                medium = np.dot(s_k,delta_f_k)
                # print(f)
                # f_k = np.asarray(instance_C.calculate(f, x_k), dtype=np.float32)
                f_k = instance_C.calculate(f, x_k)
                # f_k format list[[]]
                f_k = f_k[0][0]
                print(gamma, f_k, medium.shape)
                alpha_k = -gamma*f_k/medium
                # g_k = np.asarray(instance_D.calculate(g, x_k), dtype=np.float32)
                g_k = instance_D.calculate(g, x_k) 
                # print(type(g_k), g_k)
                #
                test4 = np.asarray(g_k) 
                test1 = np.transpose(N_k)
                # print(type(test1), test1.shape)
                test2 = np.matmul(test1,M)
                # print(type(test2), test2.shape)
                # print(type(test4), test4.shape)
                test3 = np.dot(test2,test4)
                print(x_k.shape, alpha_k.shape, s_k.shape, test3.shape)
                x_k = x_k + alpha_k * s_k - test3
                print(x_k)
                # print(type(x_k), x_k)
                # x_k = x_k + alpha_k * s_k - np.matmul(np.matmul(np.transpose(N_k),M),g_k)
            times = times + 1

    # Decide whether the vector is all zeros
    # True is all zeros
    def decision(self, s):
        zeros = np.zeros_like(s)
        return (sum(sum(zeros == s)) == s.size)
