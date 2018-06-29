import numpy as np


class fun_f (object):
    '''
    function f:
    NUM: the number of variables
    f is a non-linear function
    f = a*x^2 + b*x + c

    calculate: 
    input ndarray 
    output constant
    '''

    def __init__(self, vNUM):
        self.num = vNUM
        self.a = np.random.rand(self.num)
        self.b = np.random.rand(self.num)
        self.c = np.random.rand(1)
        

    def calculate(self, x):
        # print('f calculate')
        try:
            second = np.inner(self.a, (x*x))
            first = np.inner(self.b, x)
            constant = self.c
            return (second+first+constant)

        except:
            if(len(x)!=self.num): print('Dimension Error of x')
            else: print('Unknown Error')

    def derivative(self, x):
        '''
        Construct derivative matrix from function f
        Return value
        '''
        try:
            der = np.zeros(self.num)
            for i in range(self.num):
                der[i] = 2 * self.a[i] * x[i] + self.b[i]

        except:
            if(len(x)!=self.num): print('Dimension Error')
            else: print('Unkown Error')
        return der    
            

class Group_g(object):
    '''
    A group of constraints functions g
    '''
    def __init__(self, vNUM, gNUM):
        '''
        NUM: the number of variables
        '''
        self.vnum = vNUM
        self.gnum = gNUM
        self.group = list()
        for i in range(gNUM):
            g = fun_f(vNUM)
            g.a = np.zeros(vNUM)
            self.group.append(g)

    def calculate(self, x):
        # print('g calculate')
        groupValue = np.zeros(len(self.group))
        for i in range(len(self.group)):
            groupValue[i] = self.group[i].calculate(x)
        return groupValue
    
    def groupDisplay(self):
        matrix = np.zeros([self.gnum, self.vnum])
        for i in range(len(self.group)):
            matrix[i] = self.group[i].b
        print(matrix)

    def derivative(self):
        g = self.group
        matrix = np.zeros([len(g), self.vnum])
        for i in range(len(g )):
            for j in range(self.vnum):
                matrix[i][j] = self.group[i].b[j]
        return matrix