from __future__ import print_function
from __future__ import division

import timeit

from data import instance_iterator, print_solution

def solve(instance_path):
    print('Question 1\n')
    for instance in instance_iterator(instance_path):
        instance_name, k, P, W, C = instance
        print('Solving', instance_name)

        start_time = timeit.default_timer()
        items = knapsack(k, P, W)
        elapsed = timeit.default_timer() - start_time

        print_solution(P, W, items)
        print('Elapsed:', elapsed)
        print()

def knapsack(k, P, W):
    items = [(i, w, p / w) for i, (p, w) in enumerate(zip(P, W))]
    items = iter(sorted(items, key=lambda t: t[2], reverse=True))

    x = [0] * len(P)
    weight = 0
    while weight < k:
        i, w, _ = next(items)
        if weight + w <= k:
            x[i] = 1
            weight += w
        else:
            x[i] = (k - weight) / w
            weight = k

    return [ (i + 1, fract) for i, fract in enumerate(x) if fract > 0]
