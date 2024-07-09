import turtle
def square(t, length):
    for count in range(4):
        t.forward(length)
        t.left(90)
        
def main():
    t = turtle.Turtle()
    length = int(input("Input the length: "))
    square(t, length)

main()
