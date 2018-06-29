import numpy as np
import timeit

NUM = 1000

for i in range(10):
    a = np.random.rand(NUM)
    b = np.random.rand(NUM)
    c = np.random.rand(NUM,NUM)
    d = np.outer(a,b)
    # c = np.outer(a,b)

    print('NUM', NUM)
    start = timeit.default_timer()
    matrix = np.matmul(c,d)
    end = timeit.default_timer()

    print(start-end)

    start = timeit.default_timer()
    vector = np.matmul(a, np.matmul(b, c))
    end = timeit.default_timer()

    print(start - end)

    NUM = NUM + 1000