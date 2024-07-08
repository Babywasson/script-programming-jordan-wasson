def mean(list):
    divider = len(list)
    listSummed = sum(list)
    return listSummed/divider

def median(list):
    digitCount = len(list)
    list.sort()
    median = list[digitCount//2]
    return median


def main():
    list = []
    listNumbers = int(input("Enter the amount of digits of your list then press enter: "))
    for i in range(0, listNumbers):
        info = int(input("Enter a digit from the list then press enter: "))
        list.append(info)
    print("The list is: ", list)
    print("The mean of your list is: ", mean(list))
    print("The median of your list is: ", median(list))
main()
    
