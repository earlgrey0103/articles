#!usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: EarlGrey@codingpy.com
# Copyright: Public Domain
#

"""
Download Images from URL, Markdown Files
"""

import os
import time
import argparse
from urllib.request import urlretrieve
import urllib.parse
from io import BytesIO

import requests
from lxml.html import fromstring
from PIL import Image

from html2md import get_html


parser = argparse.ArgumentParser()
parser.add_argument('--url', help='target url page')
parser.add_argument('--selector', help='selector of html element')
parser.add_argument('--file', help='filename')


def save_base64_image(data, filename):
    import base64
    ext = data.split(';')[0].split('/')[1]
    data = data.split(',')[1]
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '=' * (4 - missing_padding)
    imgData = base64.b64decode(data)
    filename = filename + '.' + ext
    imgFile = open(filename, 'wb')
    imgFile.write(imgData)
    imgFile.close()
    return filename


def get_urls_md(filename):
    file = open(filename, 'r')
    image_urls = []
    for line in file:
        line = line.strip()
        if line.startswith('!['):
            print(line)
            line = line.split('](')[1][:-1]
            image_urls.append(line)
    return image_urls


def get_urls(url, selector):
    resp = get_html(url, selector)
    html = fromstring(resp)

    if 'weixin.qq.com' in url:
        image_urls = html.xpath('//img/@data-src')
    else:
        image_urls = html.xpath('//img/@src')
    image_urls = [normalize_image_url(url, image_url) for image_url in image_urls]
    return image_urls


def normalize_image_url(url, image_url):
    seps = ['?', '!']
    for sep in seps:
        if sep in image_url:
            image_url = image_url.split(sep)[0]

    image_url = urllib.parse.urljoin(url, image_url)
    return image_url


def download_image(image_url):
    dirname = 'tmp'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    num = 0
    if image_url.startswith('data:image'):
        filename = 'article-image-%d' % time.time()
        path = dirname + '/' + filename
        filepath = save_base64_image(image_url, path)
        print('%s downloaded.' % path)
        return filepath

    else:

        filename = image_url.split('/')[-1]
        filepath = dirname + '/' + filename
        if os.path.exists(filepath):
            return filepath
        try:
            urlretrieve(image_url, filepath)
            return filepath
        except Exception as e:
            print('cannot urlretrieve image: %s' % e)
            print('Download using requests')

            r = requests.get(image_url)
            i = Image.open(BytesIO(r.content))
            i.save(filepath)
            return filepath


def download_images(image_urls):

    num = 0
    dirname = 'tmp'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    for image_url in image_urls:

        if image_url.startswith('data:image'):
            filename = 'article-image-%d' % num
            filename = dirname + '/' + filename
            save_base64_image(image_url, filename)
            print('%s downloaded.' % filename)
            num += 1

        else:

            filename = image_url.split('/')[-1]
            filename = dirname + '/' + filename
            try:
                urlretrieve(image_url, filename)
            except Exception as e:
                print('cannot urlretrieve image: %s' % e)
                print('Download using requests')

                r = requests.get(image_url)
                i = Image.open(BytesIO(r.content))
                i.save(filename)


def main(url, selector, filename=None):
    if filename is not None:
        image_urls = get_urls_md(filename)
    else:
        image_urls = get_urls(url, selector)

    download_images(image_urls)

if __name__ == '__main__':
    args = parser.parse_args()
    url, selector, filename = args.url, args.selector, args.file
    main(url, selector, filename)
