import turtle
def drawSquare(t, x, y, length):
    """Draw a square with a given turtle t, an upper-left
        corner point (x, y), and a side's length."""
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)
        
def main():
    t = turtle.Turtle()
    inputX = int(input("Enter the value for x: "))
    inputY = int(input("Enter the value for y: "))
    length = int(input("Input the length: "))
    drawSquare(t, inputX, inputY, length)
    print("The Square is: ", drawSquare)

main()
