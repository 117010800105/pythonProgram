#draw a spiral 
import turtle
import time
length = 400
r=0.95
turtle.setup(500,500,200,200)
turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
turtle.right(270)
while length > 20:
    turtle.fd(length)
    turtle.right(90)
    turtle.fd(length)
    turtle.right(90)
    turtle.fd(length*r)
    turtle.right(90)
    turtle.fd(length*r)
    turtle.right(90)
    length = length*r*r
    

