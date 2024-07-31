def mean(lyst):
    if len(lyst) == 0:
        raise RuntimeError("List must be non-empty. ")
    return sum(lyst) / len (lyst)

def main():
    lyst = []
    lystData = int(input("Enter the amount of numbers in your list: "))
    for i in range(0, lystData):
        info = int(input("Enter a digit from the list then press enter: "))
        lyst.append(info)
    print(mean(lyst))

main()
