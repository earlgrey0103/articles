#!usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: EarlGrey@codingpy.com
# Copyright: Public Domain
#

"""
22 个重复回复的数字
974 个有效参与回复

最终获奖用户：

用户名,回复数字,回复时间
['菜头', '25', '2016-11-01 11:31:34'], 
['ltwonders', '25', '2016-11-01 11:32:53'], 
['刘海天', '25', '2016-11-01 11:35:00'], 
['弱智儿童欢乐多', '25', '2016-11-01 11:39:26'], 
['刘鸿博', '25', '2016-11-01 11:40:51']

"""

import time
from datetime import datetime
import csv

from selenium import webdriver


def login(user, password):
    url = 'https://mp.weixin.qq.com'
    driver = webdriver.Firefox()

    driver.get(url)

    user_input = driver.find_element_by_id('account')
    pwd_input = driver.find_element_by_id('pwd')
    submit = driver.find_element_by_id('loginBt')

    user_input.send_keys(user)
    pwd_input.send_keys(password)
    submit.click()

    time.sleep(10)  # 等待扫描登陆
    return driver


def go_to_comment_page(driver):
    comments = driver.find_element_by_link_text('留言管理')
    comments.click()
    time.sleep(3)

    articles = driver.find_element_by_link_text('文章管理')
    articles.click()
    time.sleep(3)

    article = driver.find_elements_by_link_text('查看')[3]
    url = article.get_attribute('href')
    driver.get(url)
    time.sleep(3)

    return driver


def get_comments(driver, page):
    driver = go_to_comment_page(driver)
    time.sleep(3)

    res = []
    while page > 0:
        comments = driver.find_elements_by_css_selector(
            'div.discuss_area')
        for comment in comments:
            username = comment.find_element_by_css_selector(
                '.user_info > strong')
            content = comment.find_element_by_css_selector('.discuss_message')
            comment_time = comment.find_element_by_css_selector(
                '.discuss_time')
            if '2016-11-04' not in comment_time.text:
                if content.text[:2].isdigit():
                    user_tuple = (
                        username.text, content.text, comment_time.text)
                    print(user_tuple)
                    res.append(user_tuple)

        next_bt = driver.find_element_by_css_selector('a.btn.page_next')
        time.sleep(3)

        if page == 1:  # 到了最后一页，不再向后翻页
            return res[::-1]

        next_bt.click()
        page -= 1

    return res[::-1]


def process_comments(data, target, num):

    comments = remove_duplicate(data)

    hit = []
    for item in w:
        if int(item[1]) == target:
            hit.append(item)

    print(hit[:num])

    return hit[:num]


def remove_duplicate(data):
    users = []
    res = []
    num = 0
    for item in data:
        if item[0] not in users:
            users.append(item[0])
            res.append(item)
        else:
            num += 1
    print('Removed  %d duplicate comments' % num)

    with open('cleaned_comments.csv', 'w') as f:
        w = csv.writer(f)
        for item in res:
            w.writerow(item)
    return res


if __name__ == '__main__':
    driver = login('username', 'pwd')
    page = 104
    data = get_comments(driver, page)

    target = 25 # 20161104 日上证指数收盘十位个位数为 25。
    num = 4
    process_comments(data, target, num)
