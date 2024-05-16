from turtle import *


#we want to paint a house
#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)       #hight of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200, 200)
pendown()
color("black")
left(30)
forward(70)
right(90)
forward(55)
right(88)
forward(70)
right(90)
forward(55)

penup()
goto(0, 200)
pendown()
right(90)
forward(70)
left(88)
forward(55)
left(90)
forward(65)
left(88)
forward(60)
exitonclick()