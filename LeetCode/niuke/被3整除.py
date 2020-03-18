# encoding: utf-8
"""
@author: vinklibrary
@contact: shenxvdong1@gmail.com
@site: Todo

@version: 1.0
@license: None
@file: 被3整除.py
@time: 2019/9/9 9:25

这一行开始写关于本文件的说明与解释
"""
# import sys
start, end = input().split()
result = 0
arrays = [start]
for i in range(int(end)-int(start)):
    arrays.append(str(int(start)+1+i))
arrays[0] = ''.join([str(x) for x in range(1,int(start)+1)])
print(arrays)
for i in range(len(arrays)):
    if int("".join(arrays[:i+1]))%3==0:
        result+=1
print(result)
