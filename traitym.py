import turtle
import time
turtle.bgcolor("pink")
def hart_arc():

    for i in range(200):

        turtle.right(1)

        turtle.forward(2)

def move_pen_position(x, y):

    turtle.hideturtle () 

    turtle.up () 

    turtle.goto(x, y) 

    turtle.down ()

    turtle.showturtle () 



turtle.setup(width=800, height=500) 

turtle.color('red', 'pink') 

turtle.pensize(3) 

turtle.speed(1)



move_pen_position(x=0,y=-180)

turtle.left(140) 




turtle.begin_fill () 


turtle.forward(224) 



hart_arc () 
turtle.left(120) 
hart_arc () 

turtle.forward(224)

turtle.end_fill () 


window = turtle.Screen()

window.exitonclick()