# Question:
# Write a Python program that accepts a sequence of whitespace separated words as
# input and prints the words after removing all duplicate words and
# sorting them alphanumerically.
#
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
#
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input. We use set container to remove duplicated
# data automatically and then use sorted() to sort the data.
#
#
# Solution:

#!/usr/bin/python3

# Question:
# Write a Python program that accepts a sequence of whitespace separated words as
# input and prints the words after removing all duplicate words and
# sorting them alphanumerically.
#
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
#
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input. We use set container to remove duplicated
# data automatically and then use sorted() to sort the data.
#
#
# Solution:

# Didn't specify the python version, so:
try:
	# required to make it work in both python2 and python3.
	input = raw_input
except:
	pass

words = input("enter words: ").split(" ")
unique = list(set(words))
unique.sort()
print(" ".join(unique))
