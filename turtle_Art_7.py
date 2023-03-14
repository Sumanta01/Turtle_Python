# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 01:55:38 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('black')
t.color('orange')
t.hideturtle()
for i in range(45):
    t.circle(60,steps=26)
    t.left(125)
    t.forward(85)
    t.right(55)