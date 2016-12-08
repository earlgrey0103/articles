#!usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: EarlGrey@codingpy.com
# Copyright: Public Domain
#
import os
import argparse
from selenium import webdriver
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('url', help='target url page')
parser.add_argument('--selector', help='selector of html element')


def element_screenshot(url, selector='pre'):

    dirname = 'tmp'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    driver = webdriver.Firefox()
    # driver = webdriver.PhantomJS()
    driver.set_window_position(0, 0)
    driver.set_window_size(900, 500)
    driver.get(url)
    elements = driver.find_elements_by_css_selector(selector)

    driver.save_screenshot('screenshot.png')
    im = Image.open('screenshot.png')
    num = 0
    total = len(elements)
    result = []
    for ele in elements:
        location = ele.location
        size = ele.size

        temp = im.copy()

        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        cropped = temp.crop((left, top, right, bottom))

        filename = dirname + '/' + 'code-%d.png' % num 
        cropped.save(filename, quality=180)
        print(num/total * 100)
        result.append(filename)

        num += 1

    driver.close()
    return result


if __name__ == '__main__':
    args = parser.parse_args()
    url, selector = args.url, args.selector or 'pre'
    element_screenshot(url, selector)
