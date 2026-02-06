splitString = "This string has been\nsplit over\nseveral\nlines."
print(splitString)

tabbedString = "1\t2\t3\t4"
print(tabbedString)
# Escaping quotes
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner siad \"No, no, 'e's uh,..he's resting\".")
# Escape using 3 double quotes
print("""The pet shop owner said "No, no, 'e's uh,...he's resting". """)

anotherSplitString = """"This string has been \
split over \
several \
lines.
"""
print(anotherSplitString)

anotherSplitStringExample = """This string has been
split over
several
lines.
"""
print(anotherSplitStringExample)

# Exercise
tabbedString = "Number 1\tThe Larch\nNumber 2\tThe Horse Chestnut"
print(tabbedString)

# Interprets the \t as a tab character and the \n as a new line
# print("C:\Users\timbuchalka\notes.txt")

# How to fix by escaping with a backslash (preferable method)
print("C:\\Users\\timbuchalka\\notes.txt")

# Or by using raw strings
print(r"C:\Users\timbuchalka\notes.txt")
