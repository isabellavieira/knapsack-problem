from __future__ import print_function

import os
import sys

def parse_instance(instance_file):
    with open(instance_file) as f:
        text = f.readlines()
        lines = [t.strip().split() for t in text]

        nb_items = int(lines[0][0])
        knapsack_size = int(lines[0][1])

        P = [0] * nb_items
        W = [0] * nb_items
        C = [set() for _ in range(nb_items)]

        for line in lines[1:]:
            if not line:
                continue
            index = int(line[0])
            profit = int(line[1])
            weight = int(line[2])
            conflict_items = {int(i) for i in line[3:]}

            P[index - 1] = profit
            W[index - 1] = weight

            for conflict in conflict_items:
                C[conflict-1].add(index)

            C[index - 1].update(conflict_items)

        return knapsack_size, P, W, C

def instance_iterator(instance_path):
    file_list = [f for f in os.listdir(instance_path)
                if f.startswith('Data') and f.endswith('.txt')]
    for filename in sorted(file_list):
        path = os.path.join(instance_path, filename)
        k, P, W, C = parse_instance(path)
        yield (filename[5:-4], k, P, W, C)

def _print_solution(nb_items_used, total_weight, total_profit, items_fractions, instance_name, question):


    if not os.path.exists("Output_Question" + str(question)):
        try:
            os.makedirs("Output_Question" + str(question))
        except OSError as exc: # Guard against race condition
                raise

    output = open((os.getcwd()+"/Output_Question"+str(question))+"/"+instance_name+".txt", "w")

    #print('{} {} {}'.format(nb_items_used, total_weight, total_profit))
    output.write('{} {} {} \n'.format(nb_items_used, total_weight, total_profit))
    items = sorted(items_fractions, key=lambda t: t[0])
    for item, fract in items:
        #print('{} {}'.format(item, fract))
        output.write('{} {}\n'.format(item, fract))

def print_solution(P, W, items_fractions, instance_name, question):
    nb_items_used = len(items_fractions)
    total_weight = sum(W[item - 1] * fract for item, fract in items_fractions)
    total_profit = sum(P[item - 1] * fract for item, fract in items_fractions)
    _print_solution(nb_items_used, total_weight, total_profit, items_fractions, instance_name, question)
