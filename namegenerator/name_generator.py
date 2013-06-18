# -*- coding: utf-8 -*-
"""Random name generator inspired by GitHub repository name suggestions."""

from os import listdir
from os.path import normpath, join, dirname
import linecache
import random

LISTS_DIR = normpath(join(dirname(__file__), 'lists'))
LISTS_SIZES_FILE = normpath(join(dirname(__file__), 'lists_sizes'))
FILES = {}
for filename in listdir(LISTS_DIR):
    FILES[filename] = normpath(join(LISTS_DIR, filename))
THEMES = {
    # 'theme.name': [sep, (files, to, use)],
    'github.repo': ['-', ('github.repo.adjectives', 'github.repo.nouns')],
    'roman.male': [' ', ('roman.male.praenomen', 'roman.male.nomen', 'roman.male.cognomen')],
    'roman.female': [' ', ('roman.female.nomen', 'roman.female.cognomen')],
}

lists_sizes = {}
with open(LISTS_SIZES_FILE) as f:
    for line in f:
        filename, count = line.strip().split(',')
        lists_sizes[filename] = int(count)


def update_lists_sizes():
    """Update LISTS_SIZES_FILE CSV file and lists_sizes global variable

    For each list file in lists directory, count lines, write to LISTS_SIZES_FILE
    and update lists_sizes[file]
    """
    with open(LISTS_SIZES_FILE, 'wb') as lists_sizes_file:
        for filename, file_path in sorted(FILES.iteritems()):
            with open(file_path) as f:
                count = len(f.readlines())
                lists_sizes_file.write('{},{}\n'.format(filename, count))
                lists_sizes[filename] = int(count)


def get_name(sep, *args):
    """Generate and return a random name based on given lists

    :keyword sep: name separator (e.g. between first and family names)
    :type sep: char
    :param args: list files to use for the generation (order matters)
    :type args: list of strings
    :return: a randomly generated name
    :rtype: string (or None if no valid files are given as args)
    """
    name = []
    for filename in args:
        try:
            line_no = random.randrange(1, lists_sizes[filename] + 1)
        except KeyError as e:
            print 'List {} does not exist'.format(e)
        else:
            name.append(linecache.getline(FILES[filename], line_no).strip())
    return sep.join(name)


def name_generator(theme='github.repo'):
    """Generate and return a random name based on chosen theme

    :arg theme: chosen theme for the name generation
    :type theme: string
    :return: a randomly generated name
    :rtype: string (or None if theme does not exist)
    """
    try:
        sep, args = THEMES[theme]
    except KeyError as e:
        print 'Theme {} does not exist.'.format(e)
    else:
        return get_name(sep, *args)


if __name__ == '__main__':
    update_lists_sizes()
    print name_generator()