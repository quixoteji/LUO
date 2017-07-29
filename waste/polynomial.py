import numpy as np

'''
Define a class for polynomial
'''

class polynomial(object):
    '''
    defination of polynomial
    '''
    def __init__(self, w, b):
        '''
        x is matrix
        number of column:   variable
        number of row:      power
        '''
        self.w = w
        self.b = b
    
    def print_polynomial(self):
        '''
        display polynomia
        n: number of column
        m: number of row
        '''
        (m, n) = self.w.shape
        s = ''
        for i in range(m):
            for j in range(n):
                s1 = str(self.w[i,j]) + 'x' +str(j)+'^'+str(i)
                s = s + '+' + s1
        
        if self.b!= 0:
            s = s + str(self.b)
            print(s)
        else:
            print(s)
    
    def gradient(self):
        gradient_w = self.w[1:]
        polynomial_gradient = polynomial(gradient_w, 0)
        return polynomial_gradient

    

        



