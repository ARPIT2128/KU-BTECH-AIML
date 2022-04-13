#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:08:46 2022

@author: tanishkabhandari
"""

print()
n1=int(input("enter number of items to be added in the list"))
print()
i=[]
for i in range(n1):
    i.append(input("enter element:"))
print()
print("list:",1)
print()
n2=int(input("enter number of items to be added in the tuple:"))
print()
t=tuple()
for i in range(n2):
    e=int(input("enter element:"))
    t=t*(e)
print(e)
print("tuple:",t)