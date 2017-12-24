# This is a Christmas Gift for my friend
# Author : LIU, YUANJIAN 
# Created at 10:00 Dec 24 2017
import turtle

screen = turtle.Screen()
screen.setup(800,600)
screen.bgcolor('pink')
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()

square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()

circle.goto(0,280)
circle.stamp()

k = 0
for i in range(1, 17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()

    if i % 4 == 0:
        x =  30*(j+1)
        circle.color('red')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()        
        k += 2

    if i % 4 == 3:
        x =  30*(j+1)
        circle.color('yellow')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp() 

square.color('brown')
for i in range(17,20):
    y = 30*i
    for j in range(3):    
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()        
        
#turtle.exitonclick()
# The following is the process of Signature 
from math import sqrt
ratio=0.6
font_height=62.5*ratio
font_width=70*ratio
font_diagnal=sqrt(font_height*font_height+font_width*font_width)
close_center=105*ratio
far_space=0.5*font_width
close_space=0.2*font_width
pen=turtle.Turtle()
pen.shape("arrow")
pen.width(7*ratio)
pen.color("orange")
pen.up()
pen.goto(70,260)
pen.down()
#Draw T
pen.forward(font_width)
pen.up()
pen.backward(0.5*font_height)
pen.right(90)
pen.down()
pen.forward(font_height)
#Draw O
pen.up()
pen.left(90)
pen.forward(close_center)
pen.left(90)
pen.forward(0.5*font_height)
pen.down()
pen.circle(0.5*font_width)
#Draw H
pen.up()
pen.right(90)
pen.forward(far_space)
pen.left(90)
pen.forward(0.5*font_height)
pen.down()
pen.right(180)
pen.forward(font_height)
pen.backward(0.5*font_height)
pen.left(90)
pen.forward(font_width*0.8)
pen.up()
pen.left(90)
pen.forward(0.5*font_height)
pen.right(180)
pen.down()
pen.forward(font_height)
#Draw X
pen.up()
pen.left(90)
pen.forward(close_space)
pen.left(90)
pen.forward(font_height)
pen.right(135)
pen.down()
pen.forward(font_diagnal)
pen.left(135)
pen.up()
pen.forward(font_height)
pen.left(135)
pen.down()
pen.forward(font_diagnal*0.95)

pen.left(135)
pen.up()
pen.forward(3*far_space)
pen.left(90)
pen.forward((0.05+2/3)*font_height)
pen.shape('circle')
pen.pensize(5*ratio)
#print(pen.position())
pen.stamp()
pen.back((0.05+1/3)*font_height)
pen.stamp()
pen.right(90)
pen.forward(1/6*font_width)
pen.left(90)
pen.forward(9/12*font_height)
pen.down()
pen.right(90)
pen.shape('arrow')
pen.speed('fastest')
for x in range(180):
    pen.forward(0.6*ratio)
    pen.right(1)
pen.hideturtle()
turtle.exitonclick()