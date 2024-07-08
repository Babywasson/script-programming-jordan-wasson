#Student's Name: Jordan Wasson
#Semester: Summer 2024
#Due Date: 6/16/2024
#Instructor's Name: Professor Michael Schnell

#This piece of the script will prompt the user for a text file, and open it. Then will close it
file = input("Input the name of the file you would like to open: ")
orgF = open(file, 'r')

#This piece of the script will output a second text file to analyze, write to, then close.
file = input("Input the name of the file you would like to create the analysis file for: ")
orgF = open(file, 'r')
analysisFile = "Analysis-" + file
anaF = open(analysisFile, 'w')

#This piece of the script will count the words, lines, and characters in the orginal file, print it to the user, and place it into the analysis file.
textdata = orgF.read()
lines = 1 + len(orgF.readlines())
words = len(textdata.split())
characters = len(textdata)
print("The amount of lines: ", lines)
print("The amount of words: ", words)
print("The amount of characters: ", characters)
anaF.write("The amount of lines: \n")
anaF.write(str(lines))
anaF.write("\nThe amount of lines: \n")
anaF.write(str(words))
anaF.write("\nThe amount of characters: \n")
anaF.write(str(characters))
orgF.close()
anaF.close()
