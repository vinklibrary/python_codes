# encoding: utf-8
"""
@author: vinklibrary
@contact: shenxvdong1@gmail.com
@site: Todo

@version: 1.0
@license: None
@file: 迷路的牛牛.py
@time: 2019/9/9 10:14

这一行开始写关于本文件的说明与解释
"""
import sys

times = int(sys.stdin.readline().strip())
lists = sys.stdin.readline().strip()
L_num = 0
for i in range(times):
    if lists[i] == 'L':
        L_num += 1
    else:
        L_num -= 1

if L_num % 4 == 0:
    print('N')
elif L_num % 4 == 1:
    print('W')
elif L_num % 4 == 2:
    print('S')
else:
    print('E')