# encoding: utf-8
"""
@author: vinklibrary
@contact: shenxvdong1@gmail.com
@site: Todo

@version: 1.0
@license: None
@file: 表达式求值.py
@time: 2019/9/9 10:42

这一行开始写关于本文件的说明与解释
"""
import sys
a, b, c = map(int, sys.stdin.readline().strip().split())
results = []

results.append(a+b+c)
results.append(a+b*c)
results.append(a*b+c)
results.append(a*b*c)
results.append(a*(b+c))
results.append((a+b)*c)

print(max(results))
