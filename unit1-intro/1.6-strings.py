# String Manipulation

# There are many ways to manipulate strings in helpful ways.


# Concatenation - chaining two strings together
# We define two string variables str1 and str2, and use the + operator to concatenate
# them together, along with a space in between. The resulting string is stored in a new
# variable str3, which is then printed to the console.
str1 = "Hello"
str2 = "world"
str3 = str1 + " " + str2
print(str3)


# Slicing - extracting a portion of a string
# We define a string variable str4 and use square brackets [] to slice the string into
# substrings. We print out three different substrings of str4 using slicing.
# In Python, indexing starts at 0, so the first character of a string is at index 0,
# the second character is at index 1, and so on. When using slicing, you specify the
# starting index and the ending index of the substring you want to extract.
# The starting index is inclusive, meaning the character at that index will be included
# in the resulting substring. The ending index is exclusive, meaning the character at
# that index will not be included in the resulting substring.
str4 = "Python is awesome"
print(str4[0:6])  # Prints "Python" (characters 0-5)
print(str4[7:9])  # Prints "is" (characters 7-8)
print(str4[10:17])  # Prints "awesome" (characters 10-16)


# Formatting - insert values into a string
# There are several ways to format strings.
name = "Hayden"
age = 29

# The % operator uses special formatting codes to insert values into the string.
# For example, %s is used to insert a string, %d for an integer, and %f for a float.
print("My name is %s and I am %d years old." % (name, age))

# The str.format() method allows you to insert values into a string by positioning
# them inside curly braces {}. You can also use positional and keyword arguments to
# specify the values to be inserted.
print("My name is {} and I am {} years old.".format(name, age))

# f-strings are a newer and better way to format strings. They are
# formatted string literals that start with the letter f before the opening quote.
# You can insert variables and expressions directly into the string by wrapping them
# in curly braces {}.
print(f"My name is {name} and I am {age} years old.")


# Additional tricks for formatting strings:

# The \n character represents a new line or line break in the output.
# This will print each word on a new line.
print("\nI \nlove \nPython")

# Some helpful String methods
# upper() - Converts a string into upper case.
name = "roo"
name = name.upper()
print(name)

# strip() - Returns a string with the whitespace trimmed off.
game = "Minecraft     "
print(game, "is fun.")
game = game.strip()
print(game, "is fun.")

# count() - Returns the number of times a specified value occurs in a string.
sentence = "The quick brown fox jumps over the lazy dog."
e_count = sentence.count("e")
print(e_count)
