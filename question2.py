from __future__ import print_function

import timeit
import numpy as np

from data import instance_iterator, print_solution

def solve(instance_path):
    print('Question 2\n')
    for instance in instance_iterator(instance_path):
        instance_name, k, P, W, C = instance
        print('Solving', instance_name)

        start_time = timeit.default_timer()
        items = knapsack(k, P, W)
        elapsed = timeit.default_timer() - start_time

        print_solution(P, W, items)
        print('Elapsed:', elapsed)
        print()

# for i from 1 to n do:
# 11     for j from 0 to W do:
# 12         if w[i] > j then:
# 13             m[i, j] := m[i-1, j]
# 14         else:
# 15             m[i, j] := max(m[i-1, j], m[i-1, j-w[i]] + v[i])

def knapsack(k, P, W):
    n = len(W)
    m = np.zeros((n, k)) - 1
    m[0,:] = 0
    m[:,0] = 0
    print(m)
    for i in range(1, n):
        for j in range(k):
            print(m)
            if W[i] > j:
                m[i, j] = m[i - 1, j]
            else:
                m[i, j] = max(m[i - 1, j], m[i - 1, j - W[i]] + P[i])
    print(m)

# http://pt.slideshare.net/JennyGalino/knapsack-problem-11648128

if __name__ == '__main__':
    # from data import parse_instance
    # k, P, W, C = parse_instance('data/Data-120-Q1.txt')
    k = 5
    P = [3,4,5,6]
    W = [2,3,4,5]
    print(k)
    items = knapsack(k, P, W)
    # print_solution(P, W, items)
