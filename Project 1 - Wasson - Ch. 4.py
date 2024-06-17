print("This program can encrypt a message.")
plainText = input("Please enter a plain text message to encrypt: ")
distanceValue = int(input("Enter distance value: "))
code = ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distanceValue
    code += chr(cipherValue)
print("Here is your encrypted message", code)
