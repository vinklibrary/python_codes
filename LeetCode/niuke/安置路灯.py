# encoding: utf-8
"""
@author: vinklibrary
@contact: shenxvdong1@gmail.com
@site: Todo

@version: 1.0
@license: None
@file: 安置路灯.py
@time: 2019/9/9 9:52

这一行开始写关于本文件的说明与解释
"""
import sys

def get_result(way_len, way_struct):
    re = 0
    i=0
    while i < way_len:
        if way_struct[i]=='.':
            re+=1
            i+=3
        else:
            i+=1
    print(re)

tests_num = int(sys.stdin.readline().strip())
results = []
for i in range(tests_num):
    way_len = int(sys.stdin.readline().strip())
    way_struct = sys.stdin.readline().strip()
    results.append(get_result(way_len, way_struct))