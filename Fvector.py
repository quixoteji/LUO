from Nmatrix import Nmatrix

class Fvector(object):
    
    def __init__(self, f, num):
        self.f = f
        self.num = num

    def delta_f_generation(self):
        delta_f = Nmatrix(self.f, self.num).N_generation()
        return delta_f

    def delta_f_calculation(self, x, delta_f):
        if len(x) == self.num:
            (r,c) = (len(delta_f), len(delta_f[0]))
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
                    value = delta_f[i][j].evalf(subs=subs_dict)
                    matrix[i][j] = value
            return matrix

        else:
            print("Something wrong with the dimension in delta_f_calculation")
            return
        
    def f_calculation(self, x):
        if len(x) == self.num:
            (r,c) = (len(self.f), len(self.f[0]))
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
                    value = self.f[i][j].evalf(subs=subs_dict)
                    matrix[i][j] = value
            return matrix

        else:
            print("Something wrong with the dimension in delta_f_calculation")
            return
        
