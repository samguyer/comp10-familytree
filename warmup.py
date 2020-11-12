
# Set of functions that call each other
#
# functionA calls functionB
# functionB calls functionC
# functionC calls functionD
# functionD calls functionE
#

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