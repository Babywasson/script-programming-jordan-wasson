import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
guessAmount = round(math.log(larger - smaller + 1, 2))
while True:
    count += 1
    print(smaller, larger)
    enduserNumber = (smaller + larger) // 2
    print("Your number is", enduserNumber)
    theAnswer = input("Enter equals, less than, or greater than: ")
    if theAnswer == "equals":
        print("HAHA you have been beaten by a PC in", count, "runs.")
        break
    elif count == guessAmount:
        print("You have won, I can no longer guess.")
        break
    elif theAnswer == "less than":
        larger = enduserNumber - 1
    else:
        smaller = enduserNumber + 1


