#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Karoll Quijano - kquijano

ABE 651 - Environmental Informatics

Think Python - Chapter 4-7
Exercise 4.2
"""

# General set of functions that can draw flowers with turtle function

import turtle

def petal(length, angle):
    ''' Draws one petal 
    
        length = length of petal
        angle = width of petal'''
    for i in range (2):                                     # Draws one petal
        turtle.circle(length,angle)
        turtle.left(180-angle)  

def flower(n, length, angle):
    ''' Draws flower using petals() function
    
        n = number of petals
        length = length of petals
        angle = width of petals'''
    for i in range (n):                                     # Draws n number of petals
        petal(length, angle)
        turtle.left(360/n)

def draw_3flowers():
    ''' Draws a sequence of 3 flowers with 7, 10, and 20 petals, respectively'''     
    flower_Set = ([7, 110, 60], [10,70,90],[20,170,30])     # n_petal, length and angle for each flower
    
    for n in range(len(flower_Set)):
        flower(flower_Set[n][0], flower_Set[n][1], flower_Set[n][2])
        turtle.up()                                         # moves turtle to the left 
        turtle.forward(210)
        turtle.pd()
           
    
draw_3flowers()
  
    
    
    
    
    
    
