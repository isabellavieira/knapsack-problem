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
        items, dp_profit = knapsack(k, P, W)
        elapsed = timeit.default_timer() - start_time

        print_solution(P, W, items)
        print('Elapsed:', elapsed)
        total_weight = sum(W[item - 1] * fract for item, fract in items)
        if total_weight > k:
            raise Exception("Erro no preenchimento da mochila.")
        total_profit = sum(P[item - 1] * fract for item, fract in items)
        if total_profit != dp_profit:
            raise Exception("Valor total nao alcancado.")
        print()

def knapsack(k, P, W):
    n = len(W)+1
    K = k+1
    m = np.zeros((n, K))
    for i in range(1, n):
        for j in range(1, K):
            if W[i-1] > j:
                m[i, j] = m[i - 1, j]
            else:
                m[i, j] = max(m[i - 1, j], P[i-1] + m[i - 1, j - W[i-1]])

    items = []
    i, j = n - 1, K - 1
    while j > 0 and m[i, j] > 0:
        p = m[i, j]
        p_ = m[i-1, j]
        while p == p_:
            i -= 1
            p_ = m[i-1,j]
        j -= W[i-1]
        if j >= 0:
            items.append((i, 1))
            i -= 1

    return items, m[-1,-1]

# if __name__ == '__main__':
#     from data import parse_instance
#     k, P, W, C = parse_instance('data/Data-120-Q1.txt')
#     # k = 7
#     # P = [1,4,5,7]
#     # W = [1,3,4,5]
#     print(k)
#     items, dp_profit = knapsack(k, P, W)
#     print("Valor total da matriz: ",dp_profit)
#     print(items)
#     print_solution(P, W, items)
