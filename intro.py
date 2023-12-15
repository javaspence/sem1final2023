import turtle
import keyboard

painter = turtle.Turtle()
screen = turtle.Screen()

screen.setup(1040, 850)
screen.screensize(1003, 800)
screen.addshape('pictures/Intro1.gif')
painter.goto(0,0)
painter.shape('pictures/Intro1.gif')
def introstart():
    painter.hideturtle()
    import final
keyboard.on_press_key("space", lambda _:introstart())
screen.mainloop()
