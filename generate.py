import argparse
import re
import random
import pickle
import collections
import sys

def rand(dic_t, value):
    words_lst = list()
    for k in list(dic_t[value]):
        for i in range(dic_t[value][k]):
            words_lst.append(k)
    return random.choice(words_lst)


def generator(first_w, le_n, model, out):
    md = open(model, 'rb')
    words = pickle.load(md, encoding='UTF-8')
    md.close()
    wrd = first_w
    if out != 'stdout':
        ou_t = open(out, 'w')
    else:
        ou_t = sys.stdout
    if wrd not in list(words.keys()):
        wrd = random.choice(list(words.keys()))
    ou_t.write(wrd + ' ')
    for i in range(le_n - 1):
        wrd = rand(words, wrd)
        ou_t.write(wrd + ' ')
    if out != 'stdout':
        ou_t.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True, help='File where your model is')
    parser.add_argument('--seed', default='', help='First word')
    parser.add_argument('--length', required=True, type=int, help='Length of the new text')
    parser.add_argument('--output', default='stdout', help='Output file')
    args = parser.parse_args()
    f = open(args.model, 'rb')
    words = dict(pickle.load(f))
    f.close()
    if args.seed == '':
        first_word = random.choice(list(words.keys()))
    else:
        first_word = args.seed
    generator(first_word, args.length, args.model, args.output)
if __name__ == '__main__':
    main()







