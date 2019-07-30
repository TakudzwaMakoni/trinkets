#QMCW turtle example


import turtle
t = turtle.Turtle()
t.speed(5)
#letter Q shell:


#outer
t.penup()
t.goto(-200,0)
t.pendown()

t.begin_fill()
t.color("blue")

t.left(90)
t.forward(100)
t.left(-90)
t.forward(70)
t.left(-90)
t.forward(85) #
########
t.goto(-150,35)
t.left(180)
t.forward(45)
t.left(90)
t.forward(30)
t.left(90)
t.forward(60)
t.left(90)
t.forward(15)
t.goto(-145,0)
t.goto(-200,0)
t.left(180)
#######

t.end_fill()
t.penup()

#end of correction


# the Q tip


t.goto(-165,20)
t.pendown()

t.begin_fill()
t.color("red")

t.goto(-165,35)
t.goto(-150,35)
t.goto(-115,0)
t.forward(30)
t.left(-90)
t.goto(-165,20)
t.end_fill()

t.penup()


#letter M
t.color("black")

t.goto(-100,0)
t.pendown()
t.forward(100)
t.left(-90)
t.forward(20)
t.goto(-60,65)
t.goto(-40,100)
t.forward(20)
t.left(-90)
t.forward(100)
t.left(-90)
t.forward(20)
t.left(-90)
t.forward(60)
t.goto(-60,5)
t.goto(-80,60)
t.left(-180)
t.forward(60)
t.left(-90)
t.forward(20)
t.left(-90)
t.penup()

#letter C



t.goto(10,0)
t.pendown()

t.begin_fill()
t.end_fill()
t.color("black")

t.forward(100)
t.left(-90)
t.forward(70)
t.left(-90)
t.forward(20)
t.left(-90)
t.forward(50)
t.left(90)
t.forward(60)
t.left(90)
t.forward(50)
t.left(-90)
t.forward(20)
t.left(-90)
t.forward(70)
t.left(-90)

t.end_fill()
t.penup()
#letter W



t.goto(110,0)
t.pendown()

t.begin_fill()
t.color("#5F054E")

t.forward(100)
t.left(-90)
t.forward(20)
t.left(-90)
t.forward(60)
t.goto(150,95)
t.goto(170,40)
t.left(180)
t.forward(60)
t.left(-90)
t.forward(20)
t.left(-90)
t.forward(100)
t.left(-90)
t.forward(20)
t.goto(150,35)
t.goto(130,0)
t.forward(20)

t.end_fill()
t.penup()



t.goto(0,-30)
t.color("black")
t.write("School of Physics and Astronomy",move=True,align="left",font=("Arial", 15,"normal") )




input()
