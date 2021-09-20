# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-22 21:05
# 《自然语言处理入门》2.3.1 完全切分
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
import os
import sys

folders = os.path.abspath(__file__ if '__file__' in globals() else '.').split(os.path.sep)
try:
    index = folders.index('tests')
    # 将tests放入path中，并且排除IPython/extensions下面的tests
    sys.path = [os.path.sep.join(folders[:index])] + [x for x in sys.path if 'IPython' not in x]
    from tests.test_utility import ensure_data
except ValueError:
    print('找不到tests目录，请将本文件放到tests下的任意子目录中运行')
    exit(1)

from tests.book.ch02.utility import load_dictionary


def fully_segment(text, dic):
    word_list = []
    for i in range(len(text)):                  # i 从 0 到text的最后一个字的下标遍历
        for j in range(i + 1, len(text) + 1):   # j 遍历[i + 1, len(text)]区间
            word = text[i:j]                    # 取出连续区间[i, j]对应的字符串
            if word in dic:                     # 如果在词典中，则认为是一个词
                word_list.append(word)
    return word_list


if __name__ == '__main__':
    dic = load_dictionary()

    print(fully_segment('商品和服务', dic))
