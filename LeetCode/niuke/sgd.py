# encoding: utf-8
"""
@author: vinklibrary
@contact: shenxvdong1@gmail.com
@site: Todo

@version: 1.0
@license: None
@file: sgd.py
@time: 2019/9/9 16:18

这一行开始写关于本文件的说明与解释
"""
import sys
import math
alpha,L2,epoch,N,M,L=map(float,sys.stdin.readline().strip().split())
train_data = []
testt_data = []
for i in range(int(M)):
    train_data.append([])
    for j in sys.stdin.readline().strip().split():
        train_data[i].append(float(j))
for i in range(int(L)):
    testt_data.append([])
    for j in sys.stdin.readline().strip().split():
        testt_data[i].append(float(j))

def LR_Train(train_data, epoch, alpha,N):
    model = [1]*int(N)
    for i in range(int(epoch)):
        for j in range(int(M)):
            for 
            print(train_data[j][0:int(N)]*model)
            tmp_result=1/(1+math.exp(sum(train_data[j][0:N]*model)))
            print(tmp_result)
        break

LR_Train(train_data, epoch, alpha, N)