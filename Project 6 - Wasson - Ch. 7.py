def myRange(stop, start, step):
    if start == "none" and step == "none":
        rangeList = []
        start = int(0)
        step = int(1)
        while start < stop:
            rangeList.append(start)
            start = start + step
        return rangeList
    elif step == "none":
        rangeList = [] 
        step = int(1)
        start = int(start)
        while start < stop:
            rangeList.append(start)
            start = start + step
        return rangeList
    else:
       rangeList = []
       step = int(step)
       start = int(start)
       while start < stop:
           rangeList.append(start)
           start = start + step
       return rangeList

def main():
    stp = int(input("Please input the stopping point of the range: "))
    strt = input("Please input the starting point of the range (input None for no value): ")
    inc = input("Please input the number you would like the data to increase by (input None for no value): ")
    myList = myRange(stp, strt, inc)
    print("Your range is: ", myList)

main()
