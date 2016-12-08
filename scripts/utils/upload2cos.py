#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: EarlGrey@codingpy.com
Copyright: Public Domain
"""

import time
import random
import hmac
import base64
import hashlib
import json
from urllib.parse import urlencode, urlsplit

import sys

import requests

APPID = '10069496'
SECRET_ID = 'AKIDmW9vrY4LasfP3mqxoJl2EhzLbvAFIV2Q'
SECRET_KEY = b'gO6lANdyMjqvsWEwGkXWYVTK3jKkz3BH'
BUCKET_NAME = 'codingpy'

BASE_URL = 'http://web.file.myqcloud.com/files/v1/'
POST_FIX = '/'.join([APPID, BUCKET_NAME]) + '/'

UPLOAD_URL = BASE_URL + POST_FIX


def generate_signature_mutli():

    r = str(random.randint(1, 10000000000))
    t = int(time.time())
    e = t + 60

    s = {
        'a': APPID,
        'b': BUCKET_NAME,
        'k': SECRET_ID,
        'e': e,
        't': t,
        'r': r,
        'f': '',
    }

    s = urlencode(s).encode('utf-8')

    signature = hmac.new(
        SECRET_KEY, s, digestmod=hashlib.sha1).digest()

    return base64.b64encode(signature + s)
   



def get_filepath(access_url):
    path = urlsplit(access_url).path[1:]

    result = '/'.join([APPID, BUCKET_NAME, path]) 
    result = '/' + result
    fileid = {
        'appid': APPID,
        'bucketname': BUCKET_NAME,
        'dirname': path.split('/')[0],
        'filename': path.split('/')[1]
    }
    fileid = urlencode(fileid)
    return result, fileid

def delete_file(filepath, fileid):
    signature = generate_signature_once(fileid)
    headers = {'Authorization': signature}
    delete_file_url = BASE_URL + filepath[1:]
    print(delete_file_url)
    files = {
        'op': 'delete'
    }
    r = requests.post(delete_file_url, headers=headers, files=files)
    resp = json.loads(r.text)
    return resp['message']


def create_dir(dirname):
    signature = generate_signature_mutli()
    headers = {'Authorization': signature}
    create_dir_url = UPLOAD_URL + dirname + '/'
    files = {
        'op': 'create'
    }
    r = requests.post(create_dir_url, files=files, headers=headers)
    resp = json.loads(r.text)
    return resp['data']['resource_path']

def list_dir(dirname, num=10):
    signature = generate_signature_mutli()
    headers = {'Authorization': signature}
    list_dir_url = UPLOAD_URL + dirname + '/'
    params = {
        'op': 'list',
        'num': num
    }
    r = requests.get(list_dir_url, headers=headers, params=params)
    resp = json.loads(r.text)
    if resp['code'] == 0:

        return resp['data']['infos']
    return None

def delete_dir(dirname):
    if list_dir(dirname):
        print('Please delete all files in the directory first')
        return
    signature = generate_signature_once(dirname)
    headers = {'Authorization': signature}
    files = {
        'op': 'delete'
    }
    delete_dir_url = UPLOAD_URL + dirname + '/'
    r = requests.post(delete_dir_url, headers=headers, files=files)
    resp = json.loads(r.text)
    return resp['message']

def delete_dir_files(dirname):
    data = list_dir(dirname)
    print(data)
    for item in data:
        access_url = item['access_url']
        filepath, fileid = get_filepath(access_url)
        print(filepath, fileid)
        r = delete_file(filepath, fileid)
        print(r)


if __name__ == '__main__':
    filename = sys.argv[1]
    resp = upload_image(filename)
    print(acess_image(resp))
