print("This program can decrypt a message.")
encodedText = input("Please enter a message to decrypt ")
distanceValue = int(input("Enter the distance value: "))
plainText = ""
for ch in encodedText:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distanceValue
    plainText += chr(cipherValue)
print("Here is the decoded text: ", plainText)
