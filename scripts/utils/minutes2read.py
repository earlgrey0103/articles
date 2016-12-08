#!usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: EarlGrey@codingpy.com
# Copyright: Public Domain
#

import sys
import itertools

WORDS_PER_MINUTE = 650


IMAGE_READ_TIME = 12  # seconds
# count 12 seconds for the first image, 11 for the second, and minus an
# additional second for each subsequent image. Any images after the tenth
# image are counted at three seconds.
# refer to https://help.medium.com/hc/en-us/articles/214991667-Read-time


def get_md_data(filename):
    with open(filename, 'r') as f:
        tmp = f.readlines()[10:]

    text = []
    images = []

    for line in tmp:
        if line == '\n' or line == '***\n':
            continue
        elif line.startswith('!['):
            images.append(line)
        else:
            text.append(line)

    return (text, images)


def minutes_to_read(text, images):
    chain = itertools.chain(*text)
    total_words = sum([len(line) for line in chain])
    print('total words: %d' % total_words)
    text_minute = total_words / WORDS_PER_MINUTE

    image_seconds = len(images) * IMAGE_READ_TIME
    image_minute = image_seconds / 60

    return text_minute + image_minute


def main():
    filename = sys.argv[1]
    text, images = get_md_data(filename)
    print(filename)
    minutes = minutes_to_read(text, images)
    print(round(minutes, 0))


if __name__ == '__main__':
    main()
