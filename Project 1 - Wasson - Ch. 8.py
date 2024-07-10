import turtle
import math

def circle(t, x, y, radius):
    t.up()
    t.setposition(x, y - radius)
    t.down()
    circumference = 2 * math.pi * radius
    for count in range(120):
        t.forward((circumference / 120.0))
        t.left(3)
        
def main():
    t = turtle.Turtle()
    radius = int(input("Input the radius: "))
    x = int(input("Input the starting x coordinate: "))
    y = int(input("Input the starting y coordinate: "))
    circle(t, x, y, radius)

main()

