variables = raw_input()
string = raw_input()

variables = variables.split(" ")
mode = variables[0]

# 5 variables for the addition/division and when to do that
a = int(variables[1])
b = int(variables[2])
c = int(variables[3])
d = int(variables[4])
e = int(variables[5])

# Shift value starts equal to the length of the string
m = len(string)

string = list(string)

encrypted = ""

decrypted = ""

offsetarray = []

processed = 0
# Don't want the mod check to run when processed is 0
first = True
# generate the array for character offsets, need for both encryption and decryption
for character in string:
    if (processed % b) == 0 and not first:
        a += c
    if (processed % d) == 0 and not first:
        a /= e
    if ord(character) != 32:
        offsetarray.append(m)
        
    else:
        offsetarray.append(0)

    m += a
    processed += 1
    first = False

count = 0

# If we're decrypting sub our offsets from the letters and make sure they're in bounds
if mode == "d":

    for character in list(string):
        number = ord(character)
        if number is not 32:  # Don't operate on spaces (ASCII value 32)
            number -= offsetarray[count]
            # Check that we aren't out of bounds
            if number >= 123:  # ASCII value of 1+z
                number = (number - 97) % 26 + 97
            while number <= 96:  # ASCII value of 1-a
                number += 26
        decrypted += chr(number)

        count += 1
    print decrypted
# If we aren't decrypting, we must be encrypting, so just add instead of subtract
else:

    for character in list(string):
        number = ord(character)
        if number is not 32:
            number += offsetarray[count]
            if number >= 123:
                number = (number - 97) % 26 + 97
            while number <= 96:
                number += 26
        encrypted += chr(number)

        
        count += 1
    print encrypted
