from Nmatrix import Nmatrix
from sympy import diff
from sympy import evalf

class Fvector(object):
    '''
    Operation on objective function f
    initial: function f, variable value x, number of variable num
    delta_f_generation: generate delta function of f
    f_calculation: use x to calculate function f
    PS:
    f_calculation can calculate the value of delta_f
    '''
    
    def __init__(self, f, num):
        self.f = f
        self.num = num

    def delta_f_generation(self):
        x_symbols = []
        for i in range(1, self.num+1):
            s = 'x' + str(i)
            x_symbols.append(s)
        # print(x_symbols)
        (r, c) = (len(self.f), self.num)
        N_matrix = [[0 for x in range(c)] for y in range(r)]
        
        r_counter =0
        for i in self.f:
            for c_counter in range(c):
                diff_ = diff(i[0], x_symbols[c_counter])
                N_matrix[r_counter][c_counter] = diff_
            r_counter = r_counter + 1
        r_counter = 0
        return N_matrix
        
    # def f_calculation(self, x):
    #     if len(x) == self.num:
    #         (r,c) = (len(self.f), len(self.f[0]))
    #         x_symbols = []
    #         for i in range(1, self.num+1):
    #             s = 'x' + str(i)
    #             x_symbols.append(s)
    #         subs_dict = {}
    #         for i in range(self.num):
    #             subs_dict[x_symbols[i]] = x[i]
    #         # print(subs_dict)

    #         matrix = [[0 for i in range(c)] for j in range(r)]
    #         # print(matrix)
    #         for i in range(r):
    #             for j in range(c):
    #                 value = self.f[i][j].evalf(subs=subs_dict)
    #                 matrix[i][j] = value
    #         return matrix

    #     else:
    #         print("Something wrong with the dimension in delta_f_calculation")
    #         return