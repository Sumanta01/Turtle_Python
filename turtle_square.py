# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:31:25 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
t.color('red')
w=turtle.Screen()
w.bgcolor('black')
t.speed(0)
t.begin_fill()
t.fillcolor('yellow')
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.hideturtle()