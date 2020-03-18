# encoding: utf-8
import sys
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

m,n = map(int,sys.stdin.readline().strip().split())
if n==1:
    print(1)
elif m==n:
    print(factorial(n))
else:
    tmp_dict={}
    tmp=4
    tmp_dict.setdefault(1,{})
    tmp_dict[1].setdefault(1,0)
    tmp_dict.setdefault(2, {})
    tmp_dict[2].setdefault(1,1)
    tmp_dict[2].setdefault(2, 2)
    tmp_dict.setdefault(3,{})
    tmp_dict[3].setdefault(1,1)
    tmp_dict[3].setdefault(2,6)
    tmp_dict[3].setdefault(3,6)
    while tmp<=m:
        tmp_dict.setdefault(tmp, {})
        for i in range(1,tmp+1):
            if i==1:
                tmp_dict[tmp].setdefault(i,1)
            elif i==tmp:
                tmp_dict[tmp].setdefault(i, factorial(tmp))
            else:
                # print(i)
                tmp_val = tmp_dict[tmp-1][i]*i+tmp_dict[tmp-1][i-1]*i
                tmp_dict[tmp].setdefault(i, tmp_val)
        tmp+=1
    # print(tmp_dict)
    print(tmp_dict[m][n])