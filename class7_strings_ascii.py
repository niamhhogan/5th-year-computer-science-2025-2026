"""
5th Year Computer Science
Class 7: Substrings and ASCII
"""

#Recap of strings
string1="Hello"
string2="World!"
print(string1+string2) #string concatenation +
print(string1*3) #string replication

name="Niamh"
fav_colour=input("What is your favourite colour?").lower().strip() 
print(f"Hello {name}, your favourite colour is {fav_colour}") #formatted string

print("HELLO".lower()) #makes it all lowercase
print("HELLO".capitalize()) #makes just the first letter capital and the rest lowercase
print("hello".upper()) #makes it all uppercase
print("    hello    ".strip()) #removed blank spaces at the start and end

#indexing 
sentence="Computer Science is the best subject"
print(len(sentence)) #len counts the amount of characters
print(sentence[0]) #indexing - gives the character at index position 0 (first)
print(sentence[5]) #prints the character in index position 5 (the 6th character)
print(sentence[-1]) #prints the last character
print(sentence[2:5]) #prints the characters from index position 2 up to but not including index position 5
print(sentence[:5])# prints the characters from the start up to but not including 5
print(sentence[::2]) #prints the first character then every second one

#Substrings
sentence="Computer Science is the best subject".lower()
print("computer" in sentence) #returns True 
print("maths" in sentence) #returns False
print(sentence.find("science")) #will give the index location of where "Science" starts
print(sentence.find("maths")) #will give results of -1 (not found)


#Finding if a substring is present
#using .__contains__()

name="Niamh"
print(name.__contains__("N")) #returns True
print(name.__contains__("s")) #returns False

#locating a substring
print(name.index("N"))
print(name.index("m"))


"""
ASCII: American Standard Code for Information Interchange
- designed in the 1960's
- Each character (letter, digit, punctuation, etc.) is stored as a number.
- Standard ASCII uses 7 bits, giving 128 characters (0–127):
    • 0–31   : control characters (e.g. newline, tab)
    • 32     : space
    • 33–47  : punctuation (e.g. ! " # $ % & ' ( ) * + , - . /)
    • 48–57  : digits 0–9
    • 65–90  : uppercase letters A–Z
    • 97–122 : lowercase letters a–z
    • 127    : delete (control character)

- 8-bit character sets can represent 256 characters (0–255).
  The first 128 are standard ASCII, and 128–255 are called extended ASCII
  which include accented letters (é, ñ) and extra symbols (£, €).

Examples:
    chr(65) -> 'A' #chr() converts ascii decimal value to character
    ord('A') -> 65 #ord() converts character to ascii decimal value
"""

#example: Converting from a character to ASCII decimal value
character="N"
ascii_decimal=ord(character)
print(type(ascii_decimal)) #prints the data type the variable ascii_char now is
print(f"The decimal value for the letter N is {ascii_decimal}")

#example: Converting from decimal to character
decimal=70
ascii_char=chr(decimal)
print(type(ascii_char))
print(f"The character represented by the decimal value of {decimal} is {ascii_char}")


"""
Encryption
-->Encryption is the process of encoding information for security purposes

"""
#Encryption Example
letter="C"
key=5
ascii_dec=ord(letter)
encrypted_letter=chr(ascii_dec+key)
print(f"The encrypted letter is: {encrypted_letter}")
