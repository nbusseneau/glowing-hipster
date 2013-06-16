# -*- coding: utf-8 -*-
"""Random name generator inspired by GitHub repository name suggestions."""

from os import listdir
from os.path import normpath, join, dirname
import linecache
import random

LISTS_DIR = normpath(join(dirname(__file__), 'lists'))
LISTS_SIZES = normpath(join(dirname(__file__), 'lists_sizes'))
FILES = {}
for filename in listdir(LISTS_DIR):
    FILES[filename] = normpath(join(LISTS_DIR, filename))


def update_lists_sizes():
    """Update lists_size CSV file

    For each list file in lists directory, count lines and add to lists_sizes
    """
    with open(LISTS_SIZES, 'wb') as lists_sizes:
        for filename, file_path in FILES.iteritems():
            with open(file_path) as f:
                count = len(f.readlines())
                lists_sizes.write('{},{}\n'.format(filename, count))


def read_lists_sizes():
    """Read lists_size CSV file and return a dict{filename: count}"""
    lists_sizes = {}
    with open(LISTS_SIZES) as f:
        for line in f:
            filename, count = line.strip().split(',')
            lists_sizes[filename] = int(count)

    return lists_sizes


def get_name(sep='-'):
    """Generate and return a random name"""
    lists_sizes = read_lists_sizes()
    line_no = random.randrange(1, lists_sizes['adjectives'] + 1)
    adjective = linecache.getline(FILES['adjectives'], line_no).strip()
    line_no = random.randrange(1, lists_sizes['nouns'] + 1)
    noun = linecache.getline(FILES['nouns'], line_no).strip()
    return sep.join([adjective, noun])


if __name__ == '__main__':
    print get_name()