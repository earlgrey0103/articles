#!usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: EarlGrey@codingpy.com
# Copyright: Public Domain
# Official SDK : https://github.com/tencentyun/cos-python-sdk

import time
import random
import hmac
import base64
import hashlib
import json
import os
from urllib.parse import urlencode, urlsplit, urljoin, quote

import sys

import requests


class File(object):

    def __init__(self, fileid):
        self.fileid = fileid


class COS(object):

    """docstring for COS"""

    def __init__(self, appid, bucket, secret_id, secret_key):
        self.appid = appid
        self.bucket = bucket
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.base_url = 'http://web.file.myqcloud.com/files/v1/'

    def create_signature(self, once=False, fileid=None):
        now = int(time.time())
        expired = 0 if once else now + 60

        sign_dict = {
            'a': self.appid,
            'b': self.bucket,
            'k': self.secret_id,
            'e': expired,
            't': now,
            'r': random.randint(1, 999999999),
            'f': fileid if once else ''
        }

        s = urlencode(sign_dict, safe='/').encode('utf-8')

        sha1_hmac = hmac.new(
            self.secret_key.encode('utf-8'), s, digestmod=hashlib.sha1).digest()
        signature = base64.b64encode(sha1_hmac + s)

        return {'Authorization': signature}


    def list_dir(self, dirname=None):
        """
        return fileids
        """
        if not dirname:
            list_url = self.base_url + '%s/%s/' % (self.appid, self.bucket)
        else:
            list_url = self.base_url + '%s/%s/%s/' % (self.appid, self.bucket, dirname)
        headers = self.create_signature()    
        params = {
            'op': 'list',
            'num': '100', # maximum?
        }
        r = requests.get(list_url, headers=headers, params=params )
        resp = json.loads(r.text)
        files = []
        dirs = []
        if resp['code'] == 0:
            data = resp['data']['infos']
            for item in data:
                if 'access_url' not in item:
                    dirs.append(dirname + '/' + item['name'] if dirname else item['name'])
                else:
                    files.append(self.get_fileid(item['access_url']))
        return files, dirs

    def list_files(self):
        """
        A list of fileids
        """
        files, dirs = self.list_dir()

        while dirs:
            dirname = dirs.pop()
            new_files, new_dirs = self.list_dir(dirname)
            files += new_files
            new_dirs = ['/'.join(dirname + item) for item in new_dirs]
            dirs += new_dirs

        return files

    def upload_file(self, filepath=None, dirname=None, fileobj=None,  overwrite=True):
        """
        QCloud COS automatically creates a directory for the file
        if the specified directory does not exist.

        Overwrites file with the same name.

        """
        filename = os.path.split(filepath)[1] 
        filename = filename if overwrite else str(time.time()) + filename

        files = {
            'filecontent': fileobj if fileobj else open(filepath, 'rb'),
            'op': 'upload',
            'insertOnly': '0' if overwrite else '1'
        }

        headers = self.create_signature()
        if not dirname:
            fileid = '/'.join([self.appid, self.bucket, filename])
            upload_url = self.base_url + fileid
        else:
            fileid = '/'.join([self.appid, self.bucket, dirname, filename])
            upload_url = self.base_url + fileid

        r = requests.post(upload_url, files=files, headers=headers)
        data = json.loads(r.text)['data']
        access_url = data['access_url']
        fileid = self.get_fileid(access_url)

        return access_url

    def delete_file(self, fileid):
        """
        Signature once
        """
        headers = self.create_signature(once=True, fileid=fileid)
        delete_url = self.base_url + fileid[1:]
        files = {
            'op': 'delete'
        }
        r = requests.post(delete_url, headers=headers, files=files)
        resp = json.loads(r.text)

        return resp['code'] == 0

    def get_fileid(self, access_url):
        filepath = urlsplit(access_url).path
        fileid = "/%s/%s" % (self.appid, self.bucket) + filepath
        return fileid

    def dir_exists(self, dirname):
        pass

    def file_stat(self, fileid):
        headers = self.create_signature()
        stat_url = self.base_url + fileid[1:]
        params = {
            'op': 'stat'
        }
        resp = requests.get(stat_url, headers=headers, params=params)
        resp = json.loads(resp.text)
        if resp['code'] == 0:
            return resp['data']
        return False

if __name__ == '__main__':
    appid = '10069496'
    secret_id = 'AKIDmW9vrY4LasfP3mqxoJl2EhzLbvAFIV2Q'
    secret_key = 'gO6lANdyMjqvsWEwGkXWYVTK3jKkz3BH'
    bucket = 'codingpy'

    cos = COS(appid, bucket, secret_id, secret_key)
    num = 0
    for i in range(20):
        filename = '%d.jpg' % num
        cos.upload_file(filepath='test/test.jpg', overwrite=False)

    num = 1
    files = cos.list_files()
    for f in files:
        print(f)
        print(cos.delete_file(f))
        print(num)
        num += 1
