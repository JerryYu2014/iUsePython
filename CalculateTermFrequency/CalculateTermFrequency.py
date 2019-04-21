
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019

from __future__ import print_function

import os
# import sys
# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import collections

# 词频统计函数（使用内置模块collections实现，输出结果按词频降序排列）
def count_feq_by_collections(s):
    s_list = s.read().replace('\n',';').split(';')
    [s_list.remove(item) for item in s_list if item in ',.，。！”“']
    # 利用collections.Counter函数统计个数
    word_dict = collections.Counter(s_list)
    return word_dict

# 词频统计函数（使用字典实现，输出结果未按词频降序排列）
def count_feq_by_dict(word_list):
    # 初始化字典变量
    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

try:
    # root = os.path.realpath(__file__)
    # print(root)

    input_path = './CalculateTermFrequency/input/'
    output_path = './CalculateTermFrequency/output/'
    input_filename = output_filename = 'keyword_1.txt'

    # 拼接输入文件路径
    input_file_path = os.path.join(input_path, input_filename)

    fileContent = open(input_file_path, 'r')
    word_list = fileContent.read().rstrip('\n').replace('\n',';').split(';')

    word_dict =  count_feq_by_dict(word_list)

    # 输出结果文件
    with open(os.path.join(output_path, output_filename), 'w') as output_file:
        for key in word_dict:
            print(key, word_dict[key])
            output_file.write(key +' '+ str(word_dict[key]) + '\n')

    # print(count_feq_by_collections(fileContent))
finally:
    if fileContent:
        fileContent.close()
