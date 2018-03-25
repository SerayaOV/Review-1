import argparse
import sys
import re
import pickle
import os
import collections


def make_dict(words):
    dict_ = dict()
    le = len(words)
    for i in range(le - 1):
        word1 = words[i]
        word2 = words[i + 1]
        if word1 not in dict_:
            dict_[word1] = collections.Counter()
        dict_[word1][word2] += 1
    return dict_


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '--input-dir', default='stdin',
                        help='Path to the directory where the text is')
    parser.add_argument('--model', default='model.txt', required=True, help='Where to save the model')
    parser.add_argument('--lc', default=False, help='To do lowercase or not to do')
    args = parser.parse_args()
    if args.lc:
        l_c = True
    else:
        l_c = False
    words = []
    di_r = args.input
    if di_r == 'stdin':
        for line in sys.stdin.readlines():
            if l_c:
                line = line.lower()
            words += re.findall(r'[A-Za-zА-Яа-я0-9]+|[.?,!@]+', line)
        with open(args.model, 'wb') as f:
                pickle.dump(make_dict(words), f)
    else:
        txtfiles = list(filter(lambda x: x.endswith('.txt'), os.listdir(di_r)))
        for file in txtfiles:
            filepath = di_r + os.sep + file
            for line in open(filepath, 'r'):
                if l_c:
                    line = line.lower()
                words += re.findall(r'[A-Za-zА-Яа-я0-9]+|[.?,!@]+', line)
            with open(args.model, 'wb') as f:
                pickle.dump(make_dict(words), f)
if __name__ == '__main__':
    main()
