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
            dict_[word1] = collections.defaultdict(int)
        dict_[word1][word2] += 1
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
