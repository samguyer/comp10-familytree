
# This is a similar set of functions except that they
# pass a list down and each function prints one element
# from the list

# EXERCISE 1
# Run the program and make sure you understand the sequence
# of statements that happens.

# EXERCISE 2
# What is the value of the variable 'd' in each function?
# Can we replace the index number with d? Try it.

# EXERCISE 3
# What happens if the list has fewer than four elements? Try
# it. Change the functions so that they check to make sure
# that the list is long enough for each index operation. That
# is, compare 'd' against the length of the list. Try it with
# lists of size 2, 3, and 4.

# EXERCISE 4
# Once again, we have a set of functions that all look almost
# identical. What happens if we make print_starting_at_0 call
# itself instead of calling print_starting_at_1? Try it on
# lists of a bunch of different sized lists.

# CHALLENGE PROBLEM
# Can you modify the print_starting_at_0 function so that it
# prints the list in REVERSE order? Think about the output
# from the first set of warmup exercises -- which statements
# appeared in reverse order?

def print_starting_at_3(d, thelist):
    v = thelist[3]
    print(v)

def print_starting_at_2(d, thelist):
    v = thelist[2]
    print(v)
    print_starting_at_3(d+1, thelist)

def print_starting_at_1(d, thelist):
    v = thelist[1]
    print(v)
    print_starting_at_2(d+1, thelist)

def print_starting_at_0(d, thelist):
    v = thelist[0]
    print(v)
    print_starting_at_1(d+1, thelist)

# ---- Program starts running here -------------------

mylist = ['lions', 'tigers', 'bears', 'oh my']
print_starting_at_0(0, mylist)
