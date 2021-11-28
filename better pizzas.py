# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 23:46:05 2021

@author: deyas
"""

import math
try:
    t=int(input())
    for i in range(t):
      n, k = list(map(int,input().split()))
      g=math.gcd(n, k)
      print(n//g)
except:
    pass