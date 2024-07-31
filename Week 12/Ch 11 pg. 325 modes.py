def frequencies(lyst):
    theDictionary = {}
    for number in lyst:
        count = theDictionary.get(number, 0)
        theDictionary[number] = count + 1
    return theDictionary

def mode(lyst):
    if len(lyst) == 0:
        raise RuntimeError("List must be non-empty. ")
    theDictionary = frequencies(lyst)
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            result = key
            break
    return result

def main():
    lyst = []
    lystData = int(input("Enter the amount of numbers in your list: "))
    for i in range(0, lystData):
        info = int(input("Enter a digit from the list then press enter: "))
        lyst.append(info)
    print(mode(lyst))

main()
