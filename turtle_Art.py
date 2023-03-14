# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 00:55:25 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('black')
t.color('darkslateblue')
t.hideturtle()
t.begin_fill()
for i in range(40):
    t.left(120)
    t.forward(160)
    t.fillcolor('red')
    t.left(45)
    t.forward(80)
    t.hideturtle()
    
t.end_fill()