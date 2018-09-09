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

n = int(input())
stu = list(map(int,input().split()))
k,d = map(int,input().split())
from copy import deepcopy

row = [0]*n
dmax = []
dmin = []
for i in range(0,k):
    dmax.append(deepcopy(row))
    dmin.append(deepcopy(row))
for nk in range(0,n):
    dmax[0][nk] = stu[nk]
    dmin[0][nk] = stu[nk]

for i in range(0,n):
    for j in range(1,k):
        for kd in range(max(0,i-d),i):
            dmax[j][i] = max(dmax[j][i], dmax[j-1][kd] * stu[i], dmin[j-1][kd] * stu[i])
            dmin[j][i] = min(dmin[j][i], dmax[j-1][kd] * stu[i], dmin[j-1][kd] * stu[i])
            print(dmax[j])
            print(dmin[j])

print(max(dmax[k-1]))