#-*- coding:utf-8 _*-
"""
@author:hql
@file: demo.py
@time: 2018/09/{DAY}
"""
"""
示例1
输入
3
7 4 7
2 50
输出
49
示例 2
36
7 -15 31 49 -44 35 44 -47 -23 15 -11 10 -21 10 -13 0 -20 -36 22 -13 -39 -39 -31 -13 -27 -43 -6 40 5 -47 35 -8 24 -31 -24 -1 
3 31
示例3
47
-41 -5 -10 -31 -44 -16 -3 -33 -34 -35 -44 -44 -25 -48 -16 -32 -37 -8 -33 -30 -6 -18 -26 -37 -40 -30 -50 -32 -5 -41 -32 -12 -33 -22 -14 -34 -1 -41 -45 -8 -39 -27 -23 -45 -10 -50 -34 
6 3
"""
def maxs(stu,d,ch):
    m = -51
    ind = -1

    for i in ch:

        l = i-d
        h = i+d+1
        if l<0:
            l=0
        if h>len(stu):
            h = len(stu)
        for s in range(l,h):
            if stu[s]>m and s not in ch:
                ind = s
                m =stu[s]

    return m,ind


def mins(stu, d, ch):
    m = 51
    ind = -1

    for i in ch:
        l = i - d
        h = i + d + 1
        if l < 0:
            l = 0
        if h > len(stu):
            h = len(stu)

        for s in range(l, h):
            if stu[s] < m and s not in ch:
                ind = s
                m = stu[s]

    return m, ind

n = int(input())
stu = list(map(int,input().split()))
k,d = map(int,input().split())
choice = []
dchoice = []
m = max(stu)
mids = stu.index(m)
n = min(stu)
nids = stu.index(m)
choice.append(mids)
dchoice.append(nids)
sum = m
dsum = n
for i in range(1,k):
    m, mids = maxs(stu, d, choice)
    n, nids = mins(stu,d, dchoice)

    if m*n>0:
        if abs(m)>abs(n):
            n = m
            nids = mids
        else:
            m = n
            mids = nids

    choice.append(mids)
    dchoice.append(nids)
    l = [sum*m,sum*n,dsum*m,dsum*n]
    print(m,mids,n,nids)
    sum = max(l)
    dsum = min(l)
    print(sum,dsum)

print(sum)