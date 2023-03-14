# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 01:52:20 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('black')
t.color('greenyellow')
t.hideturtle()
#t.begin_fill()
#t.fillcolor('lightyellow')

for i in range(50):
    t.right(130)
    t.forward(100)
    t.left(15)
    t.forward(50)
    t.hideturtle()
#t.end_fill()