# encoding: utf-8
"""
@author: vinklibrary
@contact: shenxvdong1@gmail.com
@site: Todo

@version: 1.0
@license: None
@file: 俄罗斯方块.py
@time: 2019/9/9 10:33

这一行开始写关于本文件的说明与解释
"""
import sys
columns, rows = map(int, sys.stdin.readline().strip().split())
results = [0]*columns
inputs = sys.stdin.readline().strip().split()

for i in inputs:
    results[int(i)-1]+=1
print(min(results))