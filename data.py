from __future__ import print_function

import os
import sys

def parse_instance(instance_file):
    with open(instance_file) as f:
        text = f.readlines()

        lines = [ t.strip().split() for t in text]

        nb_items = int(lines[0][0])
        knapsack_size = int(lines[0][1])

        P = [0] * nb_items
        W = [0] * nb_items
        C = []

        for line in lines[1:]:
            if not line:
                continue
            index = int(line[0])
            profit = int(line[1])
            weight = int(line[2])
            conflict_items = [int(i) for i in line[3:]]

            P[index - 1] = profit
            W[index - 1] = weight
            C.append(conflict_items)

        return knapsack_size, P, W, C

def instance_iterator(instance_path):
    file_iter = (f
                for f in os.listdir(instance_path)
                if f.startswith('Data') and f.endswith('.txt'))
    for filename in file_iter:
        path = os.path.join(instance_path, filename)
        k, P, W, C = parse_instance(path)
        yield (filename[5:-4], k, P, W, C)

def _print_solution(nb_items_used, total_weight, total_profit, items_fractions):
    print('{} {} {}'.format(nb_items_used, total_weight, total_profit))
    items = sorted(items_fractions, key=lambda t: t[0])
    for item, fract in items:
        print('{} {}'.format(item, fract))

def print_solution(P, W, items_fractions):
    nb_items_used = len(items_fractions)
    total_weight = sum(W[item - 1] * fract for item, fract in items_fractions)
    total_profit = sum(P[item - 1] * fract for item, fract in items_fractions)
    _print_solution(nb_items_used, total_weight, total_profit, items_fractions)

if __name__ == '__main__':
    # k, P, W, C = parse_instance(sys.argv[1])
    # print('Knapsack size:', k)
    # print('Profits:', len(P), P.count(0))
    # print('Weights:', len(W), W.count(0))
    # print('Conflicts:', len(C), C.count([]))
    # for instance in instance_iterator(sys.argv[1]):
    #     instance_name, k, P, W, C = instance
    #     print('Instance file:', instance_name)
    #     print('Knapsack size:', k)
    #     print('Profits:', len(P), P.count(0))
    #     print('Weights:', len(W), W.count(0))
    #     print('Conflicts:', len(C), C.count([]))
    #     print()
    # 4 12 20
    # 2 1
    # 5 1
    # 8 1
    # 12 1
    print('Internal')
    _print_solution(4, 12, 20, [(5, 1), (2, 1), (12, 1), (8, 1)])
    print('Common')
    print_solution([5] * 12, [3] * 12, [(5, 1), (2, 1), (12, 1), (8, 1)])