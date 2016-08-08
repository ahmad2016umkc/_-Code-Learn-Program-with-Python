# ---------- STRINGS ----------
# Text is stored using the string data type
# You can use type to see the data type of a value
print (type(3))
print(type(3.14))
 
# Single quotes or double are both used for strings
print(type("3"))
print(type('3'))
 
samp_string = "This is a very important string"
# Each character is stored in a series of boxes labeled with index numbers
# You can get a character by referencing an index
print(samp_string[0])
 
# Get the last character
print(samp_string[-1])
 
# Get the last character
print(samp_string[3+5])
 
# Get the string length
print("Length :", len(samp_string))
 
# Get a slice by saying where to start and end
# The 4th index isn't returned
print(samp_string[0:4])
 
# Get everything starting at an index
print(samp_string[8:])
 
# Join or concatenate strings with +
print("Green " + "Eggs")
# Repeat strings with *
print("Hello " * 5)
 
# Convert an int into a string
num_string = str(4)
 
# Cycle through each character with for
for char in samp_string:
    print(char)
 
# Cycle through characters in pairs
# Subtract 1 from the length because length is 1 more then the highest index
# because strings are 0 indexed
# Use range starting at index 0 through string length and increment by
# 2 each time through
for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])
 
# Computers assign characters with a number known as a Unicode
# A-Z have the numbers 65-90 and a-z 97-122
 
# You can get the Unicode code with ord()
print("A =", ord("A"))
 
# You can convert from Unicode with chr
print("65 =", chr(65))