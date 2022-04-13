#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:05:34 2022

@author: tanishkabhandari
"""

str=input("enter string : ")

f = {} 

for i in str: 

    if i in f: 

        f[i] += 1

    else: 

        f[i] = 1

print(f)