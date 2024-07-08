def inputFloat(prompt):
    while True:
        floatNumber = input(prompt)
        if floatNumber.isdigit or floatNumber.count(".") == 1:
            return float(floatNumber)
        else:
            print("Error: the input must consist only of digits with or without decimals.")


def main():
    f = inputFloat("Please re enter a number to convert it to a Floating Point Number: ")
    print (f)

if __name__ == "__main__":
    main()
