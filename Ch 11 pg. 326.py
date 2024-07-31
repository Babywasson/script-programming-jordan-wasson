import math

def mean(lyst):
    if len(lyst) == 0:
        raise RuntimeError("List must be non-empty. ")
    return sum(lyst) / len (lyst)

def std(lyst):
    if len(lyst) == 0:
        raise RuntimeError("List must be non-empty. ")
    average = mean(lyst)
    differences = map(lambda x: x - average, lyst)
    squares = list(map(lambda x: x ** 2, differences))
    return math.sqrt(mean(squares))

def main():
    lyst = []
    lystData = int(input("Enter the amount of numbers in your list: "))
    for i in range(0, lystData):
        info = int(input("Enter a digit from the list then press enter: "))
        lyst.append(info)
    print(std(lyst))

main()
