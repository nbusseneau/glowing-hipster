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
    """Update lists_sizes CSV file

    For each list file in lists directory, count lines and add to lists_sizes
    """
    with open(LISTS_SIZES, 'wb') as lists_sizes:
        for filename, file_path in FILES.iteritems():
            with open(file_path) as f:
                count = len(f.readlines())
                lists_sizes.write('{},{}\n'.format(filename, count))


def read_lists_sizes():
    """Read lists_size CSV file and return a dict{filename: count}

    :return: dictionary of line counts for each list file
    :rtype: dict{filename: count}
    """
    lists_sizes = {}
    with open(LISTS_SIZES) as f:
        for line in f:
            filename, count = line.strip().split(',')
            lists_sizes[filename] = int(count)

    return lists_sizes


def get_name(sep, *args):
    """Generate and return a random name based on given lists

    :keyword sep: name separator (e.g. between first and family names)
    :type sep: char
    :param args: list files to use for the generation (order matters)
    :type args: list of strings
    :return: a randomly generated name
    :rtype: string
    """
    lists_sizes = read_lists_sizes()
    name = []
    for filename in args:
        line_no = random.randrange(1, lists_sizes[filename] + 1)
        name.append(linecache.getline(FILES[filename], line_no).strip())
    return sep.join(name)


if __name__ == '__main__':
    print get_name('-', 'adjectives', 'nouns')