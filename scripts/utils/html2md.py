#!usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: EarlGrey@codingpy.com
# Copyright: Public Domain
#

import os
import argparse
import requests
import html2text
from lxml.html import fromstring, tostring

parser = argparse.ArgumentParser()
parser.add_argument('url', help='target url page')
parser.add_argument('--selector', help='selector of html element')


def html2md(html):
    """
    生成的md文件中容易出现多余的 \n
    """

    h = html2text.HTML2Text()
    h.mark_code = True
    h.escape_snob = True
    h.skip_internal_links = True
    h.decode_errors = True

    md = h.handle(html)
    return md


def get_html(url, selector=None):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    if selector is not None:
        html = fromstring(resp.text)
        res = html.cssselect(selector)[0]
        return tostring(res).decode('utf-8')
    return resp.text


def save_md(md, filename=None):
    dirname = 'tmp'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    with open('tmp/temp.md', 'w') as f:
        for line in md:
            f.write(line)


if __name__ == '__main__':
    args = parser.parse_args()
    url, selector = args.url, args.selector

    html = get_html(url, selector)
    md = html2md(html)
    save_md(md)
