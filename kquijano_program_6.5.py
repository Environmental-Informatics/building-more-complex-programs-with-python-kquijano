#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Karoll Quijano - kquijano

ABE 651 - Environmental Informatics

Think Python - Chapter 4-7
Exercise 6.5
"""


def GCD(a_,b_):
    ''' Computes the greatest common divisor (GCD) of two numbers
        if r is a reminder when a/b, them gcd(a,b) = gcd(b,r) '''
    
    ls = []                                 # reorganize the values a > b
    ls.append(a_)
    ls.append(b_)
    ls
    
    a = int(max(ls))
    b = int(min(ls))
    r = a%b                                 # Calculate remainder of a/b
    
    while r!=0:                             # Loop b/r until remainder == 0
        a=b
        b=r
        r=a%b
        if r == 0:
            GCD = b
            print('GCD (%s , %s): %s' %(a_,b_,GCD))
            break
    else:
        GCD = b
        print('GCD( %s , %s): %s' %(a_,b_,GCD))
    
    return(GCD)



a=10
b=20
gcd = GCD(a,b)