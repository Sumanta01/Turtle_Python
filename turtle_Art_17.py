# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 01:23:15 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('black')
t.color('lime')
t.hideturtle()
for i in range(37):
    t.left(143)
    t.forward(75)
    for i in range(21):
        t.right(62)
        t.forward(37)
