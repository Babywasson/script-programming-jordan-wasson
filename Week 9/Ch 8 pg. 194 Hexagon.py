import turtle
def hexagon(t, length):
    for count in range(6):
        t.forward(length)
        t.left(60)
    
def main():
    t = turtle.Turtle()
    length = int(input("Input the length: "))
    hexagon(t, length)

main()
