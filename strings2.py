parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[0:6:2]) # from 0 to 6 move along in steps of 2

number = "9,223;372:036 854;775,807"
seperators = ""
print(seperators)

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

number = input("Please enter a series of numbers, using any seperators: ")
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
# add ^sum() there to add the numbers from teh input.

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
capital = ""
# Use a for loop and an if statement to print just the capitals in the quote above.

for char in quote:
    if char.isupper():
        capital = capital + char

print(capital)







