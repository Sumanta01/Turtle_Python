# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 01:53:32 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('black')
t.color('lime')
t.hideturtle()
for i in range(35):
    t.left(165)
    t.forward(80)
    t.right(45)
    t.forward(40)
    for i in range(25):
        t.circle(30)
        t.left(142)
        t.right(45)

        