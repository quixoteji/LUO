import numpy as np
import sympy 
from Nmatrix import Nmatrix
from Fvector import Fvector
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

    def N(self):
        N_generation_matrix = Nmatrix(self.h, self.num).N_generation()
        return N_generation_matrix
                
    def delta_f(self):
        d_f = Fvector(self.f, self.num).delta_f_generation()
        return d_f

    def matrix_P(self):
        pass
    
    def s_k(self):
        pass
    

    
    
