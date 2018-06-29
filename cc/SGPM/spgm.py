import numpy as np
from sympy import symbols
from sympy import diff
from sympy import evalf
from sympy import Symbol

from operations import df
from operations import cf
from operations import mask
from operations import special
from operations import norm
from operations import decision
from operations import find_minimum
from operations import update
from operations import gf

class spgm(object):
    '''
    Secure Gradient Projection Method
    '''
    def __init__(self, init_x, gamma, f, h, b, num):
        '''
        init_x: initial value of x
        gamma:  prefixed value
        f:      minimization function
        h:      constrains functions
        b:      bias for h
        num:    number of variables
        '''
        self.init_x = np.asarray(init_x)
        self.gamma = gamma
        self.f = f
        self.h = h
        self.b = b
        self.num = num
                
    def loop(self):
        # initial all functions before the iteration
        # Step 1
        x_k = self.init_x
        gamma = self.gamma
        f = self.f
        num = self.num
        N = df(f=self.h, num=num)
        delta_f = df(f=f, num=num)
        g = gf(f=self.h,b=self.b)
        times = 0
        while 1:
            print(times)
            # every *_k represents the current value of the function
            # 4
            N_k = cf(f=N, x=x_k, num=num)
            delta_f_k = cf(f=delta_f, x=x_k, num=num)
            # 5 mask N_k
            # *_*x represents the *_* head
            (N_kx, vector_v, vector_h) = mask(N_k)
            sendtoCloud(N_kx)
            # 6
            O_kx = np.matmul(N_k, np.transpose(N_k))\
            + np.matmul(np.matmul(N_k,np.transpose(vector_h)),np.transpose(vector_v))\
            + np.matmul(vector_v, np.matmul(vector_h, np.transpose(N_k)))\
            + np.matmul(np.matmul(np.matmul(vector_v, vector_h),np.transpose(vector_h)),np.transpose(vector_v))

            # 7
            T_k = np.matmul(np.matmul(N_k,np.transpose(vector_h)),np.transpose(vector_v))\
            + np.matmul(vector_v, np.matmul(vector_h, np.transpose(N_k)))\
            + np.matmul(np.matmul(np.matmul(vector_v, vector_h),np.transpose(vector_h)),np.transpose(vector_v))

            # 8
            O_k = O_kx - T_k
            # *********************
            (Ok_apostrophe, F_k) = special(O_k)
            # *********************

            # Step 2 find the inverse of O_k
            # 10
            epsilon = 0.1
            A_k = np.ones_like(O_k)
            # 11
            while(1):
                # 12
                # 13
                # *_*x represents the *_* head
                (Okx_apostrophe, Ovector_v, Ovector_h) = mask(Ok_apostrophe)
                sendtoCloud(O_kx)
                (A_kx, Avector_v, Avector_h) = mask(A_k)
                sendtoCloud(A_kx)
                # 14
                M_kx = fromcloud()
                # 15
                # M_kx = np.matmul(M_k, np.transpose(A_k))\
                # + np.matmul(np.matmul(M_k,np.transpose(Avector_h)),np.transpose(Avector_v))\
                # + np.matmul(Ovector_v, np.matmul(Ovector_h, np.transpose(A_k)))\
                # + np.matmul(np.matmul(np.matmul(Ovector_v, Ovector_h),np.transpose(Avector_h)),np.transpose(Avector_v))
                # CHECK CHECK CHECK
                Q_k = np.matmul(np.matmul(Ok_apostrophe,np.transpose(Avector_h)),np.transpose(Avector_v))\
                + np.matmul(Ovector_v, np.matmul(Ovector_h, np.transpose(A_k)))\
                + np.matmul(np.matmul(np.matmul(Ovector_v, Ovector_h),np.transpose(Avector_h)),np.transpose(Avector_v))
                # 16
                M_k = M_kx - Q_k
                A_k_ = M_k - F_k
                if norm(A_k, A_k_) < epsilon:
                    break
                else:
                    A_k = A_k_
            # 19
            Oinv_k = A_k_
            # Step 3
            # 21
            u_k = np.matmul(N_k, delta_f_k)
            # 22
            v_k = np.matmul(Oinv_k, u_k)
            # 23
            s_k = delta_f_k - np.matmul(np.transpose(N_k), v_k)
            if decision(s_k):
                # 25
                # find the minimum lamda_k and their index
                lambda_k = v_k
                (lambda_min, index) = find_minimum(lambda_k)
                # 26
                if lambda_min >= 0:
                    # 27
                    f_k = cf(num=num, f=f, x=x_k)            
                    return (x_k, f_k)
                else:
                    N = update(N, index)
                    g = update(g, index)
                    x_k = x_k
            else:
                # calculate f(x_k)
                f_k = cf(f=f, num=num, x=x_k)
                # calculate alpha
                m1 = np.dot(s_k, delta_f_k)
                m2 = gamma*f_k
                alpha_k = -m2/m1
                # calculate g(x)
                g_k = cf(f=g,num=num,x=x_k)
                # 33 calculate w_k
                w_k = np.matmul(Oinv_k, g_k)
                # 34
                x_k = x_k + alpha_k * s_k \
                    - np.matmul(np.transpose(N_k), w_k)
        
                




        

