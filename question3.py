from __future__ import print_function

import timeit
import numpy as np

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
        print('Elapsed:', elapsed)
        total_weight = sum(W[item - 1] * fract for item, fract in items)
        if total_weight > k:
            raise Exception("Erro no preenchimento da mochila.")
        print()

def knapsack(k, P, W, C):
    items = [(i, w, p / w, c) for i, (p, w, c) in enumerate(zip(P, W, C))]
    items = iter(sorted(items, key=lambda t: t[2], reverse=True))

    x = [0] * len(P)
    weight = 0
    conflicted_items = set()
    while weight < k:
        try:
            i, w, _, c = next(items)
        except StopIteration:
            break
        if weight + w <= k and i not in conflicted_items:
            x[i] = 1
            weight += w
            conflicted_items.update(c)

    return [ (i + 1, fract) for i, fract in enumerate(x) if fract > 0]

if __name__ == '__main__':
    from data import parse_instance
    k, P, W, C = parse_instance('data/Data-120-Q1.txt')
    # k = 7
    # P = [1,4,5,7]
    # W = [1,3,4,5]
    print(k)
    items, dp_profit = knapsack(k, P, W, C)
    # print("Valor total da matriz: ",dp_profit)
    print(items)
    print_solution(P, W, items)
