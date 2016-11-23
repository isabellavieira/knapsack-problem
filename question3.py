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

def knapsack(k, P, W, C):
    # TODO
    return [(1,1)]
