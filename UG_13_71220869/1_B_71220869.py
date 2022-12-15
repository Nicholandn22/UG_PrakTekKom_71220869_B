import turtle
screen = turtle.Screen()
pen = turtle.Turtle()

pen.penup()
pen.goto(-400,-90)
pen.pendown()
pen.left(90)
pen.forward(200)
pen.right(145)
pen.fd(250)
pen.left(145)
pen.fd(200)

#angka 8
pen.penup()
pen.goto(-150, -50)
pen.pendown()
pen.circle(50)
pen.penup()
pen.goto(-150, 50)
pen.pendown()
pen.circle(50)
#angka 6
pen.penup()
pen.goto(-40, -50)
pen.pendown()
pen.circle(50)
pen.penup()
pen.pendown()
pen.circle(50,-180)
pen.left(180)
pen.fd(60)
pen.circle(-120,60)

# #angka 9
# pen.penup()
# pen.goto(60, -50)
# pen.pendown()
# pen.circle(50)
# pen.penup()
# pen.pendown()
# pen.circle(-45,-180)
# pen.right(180)
# pen.fd(60)

pen.penup()
pen.goto(60,90)
pen.pendown()
pen.right(45)
pen.circle(-50)
pen.penup()
pen.goto(70,0)
pen.pendown()
pen.right(90)
pen.forward(80)
pen.circle(-50,180)









screen.exitonclick()