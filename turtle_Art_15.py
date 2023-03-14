# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 02:18:23 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('black')
t.color('lime')
t.hideturtle()
for i in range(35):
    t.right(55)
    t.left(134)
    t.forward(80)
    for i in range(25):
        t.left(123)
        t.forward(20)
        t.right(55)