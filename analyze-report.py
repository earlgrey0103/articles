# encoding=utf-8
import jieba
import requests
from bs4 import BeautifulSoup
from bosonnlp import BosonNLP


def extract_text(url):
    """Extract html content."""
    page_source = requests.get(url).content
    bs_source = BeautifulSoup(page_source)
    report_text = bs_source.find_all('p')

    text = ''

    for p in report_text:
        text += p.get_text()
        text += '\n'

    return text


def word_frequency(text):
    from collections import Counter

    words = [word for word in jieba.cut(text, cut_all=True) if len(word) >= 2]
    c = Counter(words)

    for word_freq in c.most_common(10):
        word, freq = word_freq
        print(word.decode('utf-8'), freq)


def extract_keywords(text, top_num=10):
    """Extract Keywords."""
    # 注意：在测试时请更换为您的 API token
    nlp = BosonNLP('')
    result = nlp.extract_keywords(text, top_k=top_num)

    result_dict = {k: v for (v, k) in result}

    return result_dict


def cal_change(keywords1, keywords2):
    """Calculate keywords weight change percentage between 2015 and 2016."""
    template1 = """2016年工作报告关键词 '%s' 的权重为%f，比去年同比上升了百分之%f。"""
    template2 = """2016年工作报告关键词 '%s' 的权重为%f，比去年同比下降了百分之%f。"""

    print("本次脚本执行过程共分析了出现次数前%d的关键词" % len(keywords1))

    for k in keywords1:
        if k in keywords2:
            v1 = keywords1[k]
            v2 = keywords2[k]
            change = (v1 - v2) / v2 * 100
            # 同比增长速度=（本期发展水平-去年同期水平）/去年同期水平×100%。
            if change > 0:
                print(template1 % (k, v1, change))
            else:
                print(template2 % (k, v1, -change))
        else:
            print("关键词 '%s' 不是2015年工作报告的十大关键词，它在2016年工作报告中的权重是%f" %
                  (k, keywords1[k]))


def main():
    """Main function."""
    # 2016年和2015年工作报告，这两个网页中报告的p元素都是报告内容
    url_2016 = 'http://www.gov.cn/guowuyuan/2016-03/05/content_5049372.htm'

    text_2016 = extract_text(url_2016)

    word_frequency(text_2016)

    # keywords1 = extract_keywords(text_2016)
    # keywords2 = extract_keywords(text_2015)

    # cal_change(keywords1, keywords2)

if __name__ == '__main__':
    main()
