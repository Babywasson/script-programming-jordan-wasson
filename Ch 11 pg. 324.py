def mean(lyst):
    if len(lyst) == 0:
        raise RuntimeError("List must be non-empty. ")
    return sum(lyst) / len (lyst)

def median(lyst):
    if len(lyst) == 0:
        raise RuntimeError("List must be non-empty. ")
    copy = list(lyst)
    copy.sort()
    midpoint = len(lyst) // 2
    if len(lyst) % 2 == 1:
        return copy[midpoint]
    else:
        return mean([copy[midpoint - 1], copy[midpoint]])

def main():
    lyst = []
    lystData = int(input("Enter the amount of numbers in your list: "))
    for i in range(0, lystData):
        info = int(input("Enter a digit from the list then press enter: "))
        lyst.append(info)
    print(median(lyst))

main()
