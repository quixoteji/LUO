from sympy import evalf

class M_operation(object):
    
    def __init__(self, num):
        self.num = num

    def calculate(self, M, x):
        if len(x) == self.num:
            # print(M)
            (r,c) = (len(M), len(M[0]))
            x_symbols = []
            for i in range(1, self.num+1):
                s = 'x' + str(i)
                x_symbols.append(s)
            subs_dict = {}
            for i in range(self.num):
                subs_dict[x_symbols[i]] = x[i]

            matrix = [[0 for i in range(c)] for j in range(r)]
            # print(matrix)
            for i in range(r):
                for j in range(c):
                    value = M[i][j].evalf(subs=subs_dict)
                    matrix[i][j] = value
            return matrix
        else:
            print("Something wrong with the dimension in calculation")
            return

    def update(self, M, index):
        for i in index:
            M.pop(i)
        return M
        