number = int(input("Enter the numeric grade: "))
if number > 100 or number < 0:
    print("Error: grade must be between 100 and 0")
else:
    number = number ** 2
    print("Here is your number squared: ", number)
