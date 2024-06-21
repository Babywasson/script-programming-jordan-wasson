def isSorted(listTest):
    if len(listTest) <= 1:
        return True
    else:
        for i in range(len(listTest)-1):
            if listTest[i] >= listTest[i+1]:
                return False
        return True

def main():
    listTest = []
    listInfo = int(input("Enter the amount of digits of your list then press enter: "))
    for i in range(0, listInfo):
        info = int(input("Enter a digit from the list then press enter: "))
        listTest.append(info)
    print("The list is: ", listTest)
    print("Is the list sorted?", isSorted(listTest))
main()
