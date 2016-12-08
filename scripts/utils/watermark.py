#!usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: EarlGrey@codingpy.com
# Copyright: Public Domain

# gist: https://gist.github.com/snay2/876425

import argparse
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser()
parser.add_argument('--if', help='input file')
parser.add_argument('--of', help='output file')

def watermark_text(filename, text='编程派@codingpy.com'):
    main = Image.open(filename).convert('RGBA')

    watermark = Image.new("RGBA", main.size)

    waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")

    font_path = "fonts/HelveticaNeue.dfont"
    font = ImageFont.truetype(font_path, 16)

    width, height = main.size

    waterdraw.text((20, height-35), text, fill=(255, 255, 255, 255), font=font)

    watermask = watermark.convert("L").point(lambda x: min(x, 100))

    watermark.putalpha(watermask)

    main.paste(watermark, None, watermark)
    main.save("watermark/"+filename, "JPEG")


def watermark_overlay(image, overlay):
    background = Image.open(image)
    foreground = Image.open(overlay)
    foreground.thumbnail((128, 128), Image.ANTIALIAS)

    background.paste(foreground, foreground.size, foreground)
    background.save('test1.jpg', 'JPEG')


if __name__ == '__main__':
    # filename = sys.argv[1]
    # text = 'EarlGrey@codingpy.com'
    # watermark_image(filename, text)
    image = 'test.jpg'
    overlay = 'overlay.png'
    watermark_overlay(image, overlay)
