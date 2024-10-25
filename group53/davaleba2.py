from turtle import*

color("purple")
begin_fill()
width(6)
forward(100)
left(90)
forward(70)
left(90)
forward(100)
left(90)
forward(70)
end_fill()


color("blue")
begin_fill()
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
end_fill()

penup()
goto(-100,0)
pendown()

color("yellow")
begin_fill()
right(90)
forward(100)
right(90)
forward(70)
right(90)
forward(100)
right(90)
forward(70)
end_fill()

penup()
goto(-100,100)
pendown()

color("red")
begin_fill()
left(145)
forward(100)
right(115)
forward(100)
end_fill()


penup()
goto(-30, 0)
pendown()


color("pink")
begin_fill()
left(155)
forward(30)
left(90)
forward(30)
left(90)
forward(30)

end_fill()



exitonclick()