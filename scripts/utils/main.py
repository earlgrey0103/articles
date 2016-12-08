#!usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: EarlGrey@codingpy.com
# Copyright: Public Domain
#

import argparse

from html2md import html2md, save_md, get_html
from code2png import element_screenshot
from minutes2read import get_md_data, minutes_to_read
from download_image import get_urls, download_image
from upload2cos import upload_image
from watermark import watermark_text, watermark_overlay

# add argument

parser = argparse.ArgumentParser()
parser.add_argument('url', help='target url page')
parser.add_argument('selector', help='target selector')

args = parser.parse_args()
url = args.url
selector = args.selector

# get html, convert it to md

html = get_html(url, selector)
md = html2md(html)
save_md(md)

# find images on the url page

image_urls = get_urls(url, selector)

# upload image to COS, replace with COS access url

for image_url in image_urls:
    print(image_url)
    image_path = download_image(image_url)
    print(image_path)
    new_url = upload_image(image_path)
    print(new_url)
    md = md.replace(image_url, new_url)

# take screenshot of code blocks using selenium, firefox
# 根据 URL 生成特定文件夹及文件名
print('taking screenshots of codes')
code_pngs = element_screenshot(url)

# replace code blocks in markdown with access url

md = md.split('\n')
index = 0
new_md = []
for line in md:

    if line.startswith('[code]'):       
        code_png_path = code_pngs[index]
        new_url = upload_image(code_png_path)

        img_md = '![python code image %d](%s)' % (num, new_url)
        new_md.append(img_md)
        index += 1

    elif line.startswith('    ') or line.startswith('[/code]'):
        continue
    else:
        if '\n' in line:
            line = line.replace('\n', '')
        new_md.append(line)

new_md = '\n'.join(new_md)

save_md(new_md)


