# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 01:47:54 2023

@author: KIIT
"""

import turtle
t=turtle.Turtle()
w=turtle.Screen()
t.color('red')
w.bgcolor('black')
t.hideturtle()
t.begin_fill()

for i in range(20):
    t.forward(15)
    t.left(45)
    t.fillcolor('yellow')
    t.hideturtle()
    t.forward(25)
    t.right(90)
    t.hideturtle()
   
    
t.end_fill()

 

 
