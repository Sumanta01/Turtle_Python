# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 01:37:55 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('black')
t.color('fuchsia')
t.hideturtle()
for i in range(45):
    t.circle(60,steps=6)
    t.left(125)
    t.right(55)