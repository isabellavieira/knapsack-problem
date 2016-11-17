from __future__ import print_function

import sys
import os

import question1
import question2
import question3

QUESTIONS = {
    '1': question1.solve,
    '2': question2.solve,
    '3': question3.solve,
}

def usage():
    print('trabalho <instance_path> [ {} ]'.format(' | '.join(QUESTIONS.keys())))

def main():
    if len(sys.argv) != 3:
        print('Error: missing arguments!\n')
        usage()
        return
    if not os.path.exists(sys.argv[1]):
        print('Error: <instance_path> not found!\n')
        usage()
        return
    if sys.argv[2] not in QUESTIONS:
        print('Error: unknown question {}!\n'.format(sys.argv[2]))
        usage()
        return

    _, instance_path, question = sys.argv
    QUESTIONS[question](instance_path)

if __name__ == '__main__':
    main()
