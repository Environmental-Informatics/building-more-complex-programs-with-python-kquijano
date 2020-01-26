#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Karoll Quijano - kquijano

ABE 651 - Environmental Informatics

Think Python - Chapter 4-7
Exercise 7.1
"""


import math

def mysqrt(a):
    ''' Compute square roots of 'a' using Newton's method '''
    
    x = 2
    a=int(a)
    while True:
        y = (x+a/x)/2                                           # Newton's method
        if x == y:
            break
        x=y
    return(y)
        
def test_square_root():  
    '''  Tests Newton's method comparing it with math.sqrt() function.
         Printa a table with 'a' from 1- 9 '''
         
    header = ['a', 'mysqrt(a)', 'math.sqtr(a)', 'diff']         # Creates a header
    print ('{:<6s}{:<20s}{:<20s}{:<20s}'.format(header[0], header[1], header[2], header[3]))
    print ('{:<6s}{:<20s}{:<20s}{:<20s}'.format('-','--------','------------','----'))
   
    for a in range (1,10):
        my_sqrt = mysqrt(a)                                      # Newton's method                     
        math_sqrt = math.sqrt(a)                                 # built in function
        diff = abs(my_sqrt - math_sqrt)                          # difference 
        lst = [a, math_sqrt, math_sqrt, diff]                    # built a list to print
        print ('{:<6.1f}{:<20s}{:<20s}{:<20s}'.format(lst[0], str(lst[1]), str(lst[2]), str(lst[3])))
    

test_square_root()









    
