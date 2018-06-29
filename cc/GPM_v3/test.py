import numpy as np
import datetime
from operations import cf
from operations import cg
from operations import df

num = 3
# init_x = [1 for i in range(num)]
init_x = [1,1,1]
gamma = 0.05
f = [[1,2,3],[4,5,6],[7,8,9]]
h = [[[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]],
    [[13,14,15],[16,17,18]]]

b = [10,11,12]

N = 3
class A():
    def __init__(self, x):
        self.x = x + N
    def pA(self):
        print(self.x)

a = A(3)
a.pA()
# x = cf(f=f, x=init_x)
# print(x)

# y = cg(g=h,b=b,x=init_x)
# print(y)


# def main():
#     print('begin')
#     begin = datetime.datetime.now() 
#     print(begin)
#     instance_gpm = GPM(init_x=init_x, \
#     gamma=gamma, h=h, f=f, \
#     num=num, b=b)
#     (x, fx) = instance_gpm.loop()
#     print(x)
#     print(fx)
#     print(datetime.datetime.now()-begin)

# if __name__ == '__main__':
#     main()