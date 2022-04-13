#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:59:52 2022

@author: tanishkabhandari
"""

num=int(input("enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
    