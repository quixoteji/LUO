import numpy as np

# x = np.array([0,0,0,2])
# y = np.array([0,0,0,0])
# z = np.array([1,0,0,2])

# # print(sum(x==y))
# def decision(s):
#     zeros = np.zeros_like(s)
#     # print(zeros)
#     return (sum(zeros == s) == s.size)

# print(decision(x))
# print(decision(y))
# print(decision(z))

N_k = [[2.00000000000000, 2.00000000000000, 2.00000000000000], 
        [4.00000000000000, 2.00000000000000, 2.00000000000000], 
        [2.00000000000000, 8.00000000000000, 2.00000000000000], 
        [3.00000000000000, 2.00000000000000, 6.00000000000000]]
print(N_k)
test1 = np.transpose(N_k)
print(test1)
test2 = np.matmul(N_k,test1)
print(test2)
M = np.linalg.inv(test2)
print(M)

print(f)
                f_k = np.asarray(M_operation(self.num).calculate(f, x_k),dtype=np.float32)
                print(f_k)
                alpha_k = -gamma*f_k/medium
                g_k = np.asarray(M_operation(self.num).calculate(g, x_k),dtype=np.float32)