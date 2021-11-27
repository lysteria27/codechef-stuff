# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 20:13:52 2021

@author: deyas
"""

try:
    t=int(input())
    for i in range(t):
      p=0
      n, k = list(map(int,input().split()))
      total_k=k
      if n%k==0:
        print(n//k)
      else:
        for j in range(2, n+1):
            if (k*j)%n==0 :
                break
        print(j)
except:
    pass