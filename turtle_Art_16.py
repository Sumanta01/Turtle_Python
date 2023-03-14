# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:17:17 2023

@author: KIIT
"""

import turtle
import math
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('black')
t.color('lime')
t.hideturtle()
for i in range(20):
    t.forward(85)
    t.left(127)
    t.forward(45)
    t.right(43)
    t.circle(43,steps=4)
    for j in range (13):
        t.right(33)
        t.forward(35)
        t.left(85)
        
        
   