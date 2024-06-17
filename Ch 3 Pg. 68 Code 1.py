number = int(input("Enter the numberic grade: "))
if number > 100:
    print("Error: grade must between 100 and 0")
elif number < 0:
    print("Error: grade must between 100 and 0")
else:
    print("Your score is within range.")
