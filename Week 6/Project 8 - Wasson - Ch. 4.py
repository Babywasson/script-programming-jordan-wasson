orginalFile = input("Enter the file name of the file you want to copy from: ")
newFile = input("Enter the file name of the file you want to copy to: ")
f = open(orginalFile, 'r')
g = open(newFile, 'w')
for line in f:
    g.write(line)
f.close()
g.close()
print("You have sucessfully copied your data!")
