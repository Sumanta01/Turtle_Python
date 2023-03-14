# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:42:23 2023

@author: KIIT
"""

import turtle
w=turtle.Screen()
w.bgcolor('black')
t=turtle.Turtle()
t.color('red')
t.circle(25)
t.circle(70)
t.circle(-60)
t.reset()
t.color('red')
t.hideturtle()
t.circle(100,180)
t.reset()
t.color('red')
t.begin_fill()
t.fillcolor('blue')
t.circle(100,steps=3)
t.end_fill()
t.hideturtle()
t.reset()
t.color('red')
t.begin_fill()
t.fillcolor('green')
t.circle(80,steps=5)
t.end_fill()
t.reset()
t.color('red')
t.begin_fill()
t.fillcolor('orange')
t.circle(90,steps=10)
t.end_fill()
t.hideturtle()