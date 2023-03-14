# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 02:03:33 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('black')
t.color('cyan')
t.hideturtle()
for i in range(45):
    t.circle(60,steps=56)
    t.left(125)
    t.forward(85)
    t.right(55)