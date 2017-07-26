from sympy import symbols
from sympy.abc import x,y,z
from sympy import diff
from sympy import symbols

(x1, x2, x3) = symbols('x1 x2 x3')


a = x1**2+x2**3+x3**2+x1*x3
b = x1**2-x2+x3+x1*x2
c = x1**2-2*x2**2-3*x3**3+x1*x2
d = 2*x1**2+2*x2**4-x3**4+x2*x3

result = (a*b)+(c*d)

value = result.subs(x1,1)

# matrix = [[a,b],[c,d]]
# print(matrix)
# print(matrix[0][0])
# matrix = [[x1,x1],
# [x1,x1]]
matrix = [[0,0],[0,0]]
matrix[0][0] = a  
print(matrix)
# value_all = value.evalf(subs={x1:1,x2:2,x3:3})
# print(result.expand()) 
# print(value_all)

# test_diff = [diff(a, x1), diff(b, x2)]
# print(test_diff)