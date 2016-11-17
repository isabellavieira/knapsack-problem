from __future__ import print_function

import timeit

from data import instance_iterator, print_solution

def solve(instance_path):
    print('Question 3\n')
    for instance in instance_iterator(instance_path):
        instance_name, k, P, W, C = instance
        print('Solving', instance_name)

        start_time = timeit.default_timer()
        items = knapsack(k, P, W, C)
        elapsed = timeit.default_timer() - start_time

        print_solution(P, W, items)
        print('Elapsed: {:.6f}'.format(elapsed))
        print()

def knapsack(k, P, W, C):
    # TODO
    return [(1,1)]
