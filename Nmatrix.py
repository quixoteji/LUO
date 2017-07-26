import numpy as np
from sympy import diff
from sympy import evalf

class Nmatrix(object):
    '''
    Generate the matrix of N
    N should be a polynomial matrix
    '''
    def __init__(self, h, num):
        '''
        h:  constrain functions
        num:number of variables    
        '''
        self.h = h
        self.num = num

    def N_generation(self):
        # print('N_generate OK')
        '''
        N_generation is also to do partial diff on any function
        '''
        x_symbols = []
        for i in range(1, self.num+1):
            s = 'x' + str(i)
            x_symbols.append(s)
        # print(x_symbols)
        (r, c) = (len(self.h), self.num)
        N_matrix = [[0 for x in range(c)] for y in range(r)]
        
        r_counter =0
        for i in self.h:
            for c_counter in range(c):
                diff_ = diff(i[0], x_symbols[c_counter])
                N_matrix[r_counter][c_counter] = diff_
            r_counter = r_counter + 1
        r_counter = 0
        return N_matrix

    def N_calculation(self, x):
        '''
        Based on current value of x 
        calculate the value of matrix N
        '''
        if len(x) == self.num:
            (r,c) = (len(self.h), len(self.h[0]))
            x_symbols = []
            for i in range(1, self.num+1):
                s = 'x' + str(i)
                x_symbols.append(s)
            subs_dict = {}
            for i in range(self.num):
                subs_dict[x_symbols[i]] = x[i]
            # print(subs_dict)

            matrix = [[0 for i in range(c)] for j in range(r)]
            # print(matrix)
            for i in range(r):
                for j in range(c):
                    value = self.h[i][j].evalf(subs=subs_dict)
                    matrix[i][j] = value
            return matrix

        else:
            print("Something wrong with the dimension in N_calculation")
            return 





        