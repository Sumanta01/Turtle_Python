# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 18:25:00 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.bgcolor('black')
t.color('cyan')
t.hideturtle()
t.begin_fill()
t.fillcolor('darkred')
for i in range(10):
    t.circle(55,steps=4)
   # t.forward(100)
    t.left(115)
   # t.forward(50)
    t.right(25)
    
    
t.end_fill()
