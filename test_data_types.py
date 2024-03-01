import math

# String
# literal assignment
first = "Giu"
last = "Falcaro"

print(type(first))

# check var types
if type(first) == str:
    print("is string")

if isinstance(first, str):
    print("is instance string")

# constructor
car = str("ferrari")

if type(car) == str:
    print("is car string")

if isinstance(car, str):
    print("is car instance string")

# concat strings
fullname = first + " " + last
print(fullname)
# add to the end
fullname += "!"
print(fullname)

# casting
decade = str(1990)
print(decade)
print(isinstance(decade, str))

# multiple lines
multiple = """
Hello

hi
        ok
"""
print(multiple)

# scape special characters
sentence = "I'm"  # or 'I\'m'
print(sentence)


# String Methods
print(first)
print(first.lower())
print(first.upper())

print(multiple.title())
print(multiple.replace("ok", "good"))
print(len(multiple))  # count chars
print(multiple.strip())  # remove white space on the begining and the end
print(multiple.rstrip())  # remove white space end (right)
print(multiple.lstrip())  # remove white space begining (left)
print(" ")
print("menu".center(20, "="))  # prints ========menu========
print(" ")

# string index values
print(first[0])
print(first[-1])  # last value of the string
print(first[0:2])  # return chars from position 1 to position 2
print(first.startswith("G"))
print(first.endswith("u"))

# boolean data types
isTrue = True
isFalse = bool(False)

# numeric data types
price = 100
best_price = int(80)

# float
gpa = 3.28
y = float(1.14)

# complex type
comp_value = 5 + 3j
print(comp_value)
print(comp_value.real)
print(comp_value.imag)

# Number methods
print(abs(gpa))  # get's absolute value
print(abs(gpa * -1))  # it's never negative

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))  # rounds up
print(math.floor(gpa))  # rounds down

# cast string to number
zipcode = "15990626"
zip_value = int(zipcode)
print(isinstance(zip_value, int))
