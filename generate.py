import argparse
import re
import random
import pickle
import collections


def rand(dic_t, value):
    su_m = 0
    for k in dic_t[value]:
       su_m += dic_t[value][k]
    val = random.choice(range(1, su_m))
    su_m = 0;
    for k in dic_t[value]:
        su_m += dic_t[value][k]
        k = k
        if su_m >= val:
            return k


def generator(first_w, le_n, model, out):
    words = pickle.load(model)
    if out != 'stdout':
        open(out, 'w')
    wrd = first_w
    if out != 'stdout':
        out.write(wrd)
        out.write(' ')
    else:
        sys.stdout.write(wrd)
        sys.stdout.write(' ')
    for i in range(le_n - 1):
        if not wrd in words:
            wrd = random.choice(words.values)
            if out != 'stdout':
                   out.write(wrd)
                   out.write(' ')
            else:
               sys.stdout.write(wrd)
               sys.stdout.write(' ')
        else:
            wrd = rand(words, wrd)
            if out != 'stdout':
                   out.write(wrd)
                   out.write(' ')
            else:
               sys.stdout.write(wrd)
               sys.stdout.write(' ')
    if out != 'stdout':
        out.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True, help='File where your model is')
    parser.add_argument('--seed', default='', help='First word')
    parser.add_argument('--length', required=True, type=int, help='Length of the new text')
    parser.add_argument('--output', default='stdout', help='Output file')
    args = parser.parse_args()
    words = pickle.load(args.model)
    if args.seed == '':
        first_word = random.choice(words.values)
    else:
        first_word = args.seed
    generator(first_word, args.length, args.model, args.output)
if __name__ == '__main__':
    main()
