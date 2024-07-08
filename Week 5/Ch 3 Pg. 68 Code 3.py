number = int(input("Enter the numeric grade: "))
if number >= 0 and number <= 100:
    number = number ** 2
    print("Here is your number squared: ", number)
else:
    print("Error: grade must be between 100 and 0")
