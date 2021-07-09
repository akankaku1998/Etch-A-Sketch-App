from turtle import Turtle, Screen

k = Turtle()
screen = Screen()
instruction = screen.textinput(title="INSTRUCTION", prompt="w = forward\ns = backward\na = counter-clockwise\nd = clockwise\nc = clear the window\nPress enter to start")



def forwards():
  k.forward(10)


def backwards():
  k.backward(10)


def counter_clockwise():
  k.setheading(k.heading()+10)


def clockwise():
  k.setheading(k.heading() - 10)


def clear_drawing():
  k.clear()
  k.home()
  k.clear()


screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
