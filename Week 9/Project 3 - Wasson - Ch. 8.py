import turtle

def fractalEdge(length, angle, level):
    if level == 0:
        turtle.left(angle)
        turtle.forward(length)
        turtle.right(angle)
        return
    fractalEdge(length, angle, level - 1)
    fractalEdge(length, angle + 60, level - 1)
    fractalEdge(length, angle - 60, level - 1)
    fractalEdge(length, angle, level - 1)

def kochSnowflake(width, levels):
    fractalEdge(width, 0, levels)
    fractalEdge(width, -120, levels)
    fractalEdge(width, 120, levels)


def main():
    width = int(input("Please input the width choose between 5 - 10: "))
    kochSnowflake(width, 4)
    
main()
