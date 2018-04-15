import argparse
import sys
import re
import pickle
import os
import collections
import functools


def make_dict(words):
    dict_ = collections.defaultdict(functools.partial(collections.defaultdict, int))
    length = len(words)
    couples = zip(words[:length - 1], words[1:])
    for i in couples:
        dict_[i[0]][i[1]] += 1
    return dict_


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '--input-dir', default='stdin',
                        help='Path to the directory where the text is')
    parser.add_argument('--model', default='model.txt', required=True, help='Where to save the model')
    parser.add_argument('--lc', default=False, help='To do lowercase or not to do')
    args = parser.parse_args()
    lowercase = False
    if args.lc:
        lowercase = True
    words = []
    input_dir = args.input
    if input_dir == 'stdin':
        for line in sys.stdin.readlines():
            if lowercase:
                line = line.lower()
            words += re.findall(r'[A-Za-zА-Яа-я0-9]+|[.?,!@]+', line)
    else:
        txtfiles = list(filter(lambda x: x.endswith('.txt'), os.listdir(input_dir)))
        for file in txtfiles:
            filepath = input_dir + os.sep + file
            for line in open(filepath, 'r'):
                if lowercase:
                    line = line.lower()
                words += re.findall(r'[A-Za-zА-Яа-я0-9]+|[.?,!@]+', line)
    with open(args.model, 'wb') as f:
        pickle.dump(make_dict(words), f)
if __name__ == '__main__':
    main()





