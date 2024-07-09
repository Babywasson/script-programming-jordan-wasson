import turtle
def hexagon(t, length):
    for count in range(6):
        t.forward(length)
        t.left(60)

def radialHexagons(t, n, length):
    for count in range(n):
        hexagon(t, length)
        t.left(360/ n)
        
def main():
    t = turtle.Turtle()
    length = int(input("Input the length: "))
    n = int(input("Input the n: "))
    radialHexagons(t, n, length)

main()
