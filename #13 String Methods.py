#string Methods
#strings are immutable.
# any method on string takes a copy of the object.
Name="aniket Nehe !!!"

# 3.string.upper will convert the string to an upper case
print("3: ",Name.upper())

# 4.string.lower will convert the string to lower case
print( "4: ",Name.lower())

# 5.string.rstrip("character") will Remove the trailing characters of string
print("5: ",Name.rstrip("!")) 

# 6.string.replace("character/alphabets", new character/alphabets") will replace the existing specified alphabets in string with new ones
print("6: ",Name.replace("Aniket","Aniii"))

# 7.string.split splits the string at the given alphabet and returns a list of items
print("7: ",Name.split())

# 8.string.capitalize capitalizes the first character of the word and turns rest all the characters to lower case
print("8: ",Name.capitalize())

# 9.string.center center aligns the string by adding the number of spaces mentioned in parenthesis
print("9: ",Name.center(50))

# 10.string.count counts the total number of a particular set of characters in a string
print("10: ",Name.count("e"))

# 11.string.endswith checks whether a string ends with the specific characters
print("11: ",Name.endswith("!!!"))

# 12.string.find finds the first occurrence of a given value and return the index value of the position of that occurrence
str="My Name is Aniket Nehe"
print("12: ",str.find("is"))

# 13.string.index finds the occurrence of a given value and returns the index value of the position however, if it is unable to find it will give an error causing the program to exit
str="My Name is Aniket Nehe"
print("13: ",str.index("A"))

# 14.string.isalnum checks to find if string is alphanumeric and returns true or false
str="Welcome12"
print("14: ",str.isalnum())

# 15.string.isalpha checks if there are any numbers in the string return false
str="AniketNehe"
str1="Aniket Nehe12"
print("15: ",str.isalpha())
print("15: ",str1.isalpha())

# 16.string.islower checks if there are only lower aphabets in the string
str="aniket"
print("16: ",str.islower())

# 17. string.isprintable checks if all the characters are printable in the string(non printable characters e.g \n)
str="My Name is Aniket Nehe"
str1="My Name is Aniket Nehe\n" #\n is not a printable string
print("17: ",str.isprintable())
print("17: ",str1.isprintable())

# 18 string.isspace checks if any space bar has been used in the string
str="     "
str1="anii      nehe"
print("18: ",str.isspace())
print("18: ",str1.isspace())

# 19.string.istitle The istitile() returns True only if the first letter of each word of the string is capitalized,else return false 
str="My Name Is Aniket Nehe" 
print("19: ",str.istitle())

# 20. string.isupper checks if all characters are uppercase in a string
str="ANIKET NEHE"
str1="Aniket Nehe"
print("20: ",str.isupper())
print("20: ",str1.isupper())

# 21. string.startswith checks if a string starts with a given value
str="This is a python code"
print("21: ",str.startswith("This"))

# 22. string.swapcase convert uppercase to lowercase and vice versa in a string
str="Aniket Nehe"
print("22: ",str.swapcase())

# 23.string.title converts first character of all the words in the sentence to capital
str="my Name is Aniket nehe"
print("23: ",str.title())