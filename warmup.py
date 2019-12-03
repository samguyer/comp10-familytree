
# Set of functions that call each other
#
# functionA calls functionB
# functionB calls functionC
# functionC calls functionD
# functionD calls functionE
#
# EXERCISE 1:
# Run the program and look at the output. What is the sequence of
# statements that happens? Why do the numbers go up and then go
# back down? What does the value of "d" represent? Think about
# how the second test (starting at functionB) differs from the first.

# EXERCISE 2:
# Modify these functions so that no matter where we start, it only
# goes three levels deep (that is, stop when d is 3).

# EXERCISE 3:
# Notice that the functions are almost identical. Do we really need
# all of these identical functions? What happens if change functionA
# so that instead of calling functionB, it calls ITSELF. Try it.
# A function that calls itself is called a RECURSIVE function.

def functionE(d):
    print('Start function E value is ' + str(d))
    print('Done  function E value is ' + str(d))


def functionD(d):
    print('Start function D value is ' + str(d))
    functionE(d+1)
    print('Done  function D value is ' + str(d))


def functionC(d):
    print('Start function C value is ' + str(d))
    functionD(d + 1)
    print('Done  function C value is ' + str(d))


def functionB(d):
    print('Start function B value is ' + str(d))
    functionC(d + 1)
    print('Done  function B value is ' + str(d))


def functionA(d):
    print('Start function A value is ' + str(d))
    functionB(d + 1)
    print('Done  function A value is ' + str(d))

# ---- Program starts running here -------------------

print(' ---- TEST 1 ----------')
functionA(1)

print(' ---- TEST 2 ----------')
functionB(1)