#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:52:58 2017

@author: vyk35227
"""
    
m = input("Zadej text > ").upper()
while True:
    n = int(input("Zadej číslo posunu > "))
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = a[n:] + a[:n]
    f = 0
    
    
    if " " in m:
        m = m.replace(" ","")
        
    for i in m:
        g = m[f]
        f = f + 1
        x = b[a.index(g)]
        print(x, end="")
