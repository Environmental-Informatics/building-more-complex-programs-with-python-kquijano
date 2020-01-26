#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Karoll Quijano - kquijano

ABE 651 - Environmental Informatics

Think Python - Chapter 4-7
Exercise 5.2
"""


def check_fermat(a,b,c,n) :
    ''' Takes a,b,c,n, parameters and checks if Fermat's theorem holds
        for n greater than 2, 
        a, b, c positive integers,
        and  a^n + b^n = c^n             '''
    
    if n<=2 or (isinstance(n, int)) != True:                    # Checks if n is integer greater than 2
        print('Sorry, n must be integer greater than 2')
    
    else:
        for check in a, b, c:                                   # Checks if a, b, c are positive integers
            if check<0 or (isinstance(check, int)) != True:
                print('Sorry, %.2f must be a possitive integer' %(check))
                break
                
        else:                                                    # Calculates Fermat's theorem
            a_n = a**n
            b_n = b**n
            c_n = c**n
            
            if a_n + b_n == c_n:                        
                print ('Holy smokes, Fermat was wrong!')
            else:
                print ("No, that doesn't work")
    
        
# Exercise 5.2.2

def user_inputs():
    ''' Prompts user to input values for a,b,c,n 
        converts them to integers and checks Fermat's theorem'''
    
    print(80*'-')
    print("\nFermat's Last Theorem: \n\n\
          says that there are no positive integers a, b, and c, such that:\n\
          a^n + b^n = c^n \n\
          for any value grater than 2\n")
    print(80*'-')
   
    while True:                                             # Inputs must be integers
        try:
            a,b,c,n = int(input('Enter\n\na:')), int(input('b:')), int(input('c:')), int(input('n:'))
            break
        except:
            print('\nNot an integer. Try again.')
            
    check_fermat(a,b,c,n)                                   # Checks if Fermat's theorem holds
    
    

user_inputs()