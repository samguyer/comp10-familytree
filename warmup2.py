
# This is a similar set of functions except that they
# pass a list down and each function prints one element
# from the list

# -- Print element 3 of a list
def print_starting_at_3(d, thelist):
    v = thelist[3]
    print(v)

# -- Print element 2, then call function to print 3
def print_starting_at_2(d, thelist):
    v = thelist[2]
    print(v)
    print_starting_at_3(d+1, thelist)

# -- Print element 1, then call function to print 2 and 3
def print_starting_at_1(d, thelist):
    v = thelist[1]
    print(v)
    print_starting_at_2(d+1, thelist)

# -- Print element 0, then call function to print 1,2,3
def print_starting_at_0(d, thelist):
    v = thelist[0]
    print(v)
    print_starting_at_1(d+1, thelist)

# ---- Program starts running here -------------------

mylist = ['lions', 'tigers', 'bears', 'oh my']
print_starting_at_0(0, mylist)
