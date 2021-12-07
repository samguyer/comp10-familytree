
# -- Find a person by name
#    Given a list of people (list of tuples of form name, parent1, parent2)
#    Find the person with the given name, or return None
def find_person(name, people):
    for p in people:
        if p[0] == name:
            return p
    return None

# -- Read family tree file
#    The file is a list of lines, one for each person in the family.
#    The first word on the line is the person's name; the second and
#    third names on the line are the person's parents (possibly unknown)
#    NOTE: We assume that the file is ordered so that a person's parents
#          are on earlier lines, so that they are already there when
#          we look them up.
def read_family_file(familyfile):
    people = []
    with open(familyfile) as f:
        for line in f:
            names = line.rstrip().split(' ')
            parent1 = find_person(names[1], people)
            parent2 = find_person(names[2], people)
            person = (names[0], parent1, parent2)
            people.append(person)
    return people

# -- Return the father of p
def father_of(p):
    return p[1]

# -- Return the mother of p
def mother_of(p):
    return p[2]

# ---- Coding problems here ----------------------------------------
#
# Replace "return False" with code that will compute the right
# answer for the given question.

# -- Return True if p1 is the mother of p2
def is_mother(p1, p2):
    return False

# -- Return True if p1 is the parent of p2
def is_parent(p1, p2):
    return False

# -- Return True if p1 and p2 are siblings
def is_sibling(p1, p2):
    return False

# -- Return True if p1 and p2 are cousins
#    Try Jonah and Owen (True), David and Aliza (False), and
#    Ellyn and Jane (False, should not cause an error)
def is_cousin(p1, p2):
    return False

# === STOP HERE =============================================

# -- Print out a person's grandparents
#    Make sure to check for 'None' where appropriate
def print_grandparents(p):
    return

# -- Print out a person's great grandparents
#    Make sure to check for 'None' where appropriate
def print_great_grandparents(p):
    return

# -- Print out a person's ancestors (all of them,
#    up to the point where we hit 'None'
def print_ancestors(p):
    return

# === STOP HERE =============================================

# -- Return True is p1 is the maternal grandmother of p2
#    Try Jane and Jonah (True), Jane and Jacob (False), and
#    Jane and Ethel (False, should not cause error)
def is_maternal_grandmother(p1, p2):
    return False

# -- Return True is p1 is the maternal great grandmother of p2
#    Try Isabel and Jonah (True)
def is_maternal_great_grandmother(p1, p2):
    return False

# -- Return True is p1 is the maternal great great grandmother of p2
#    Try Nora and Jonah
def is_maternal_great_great_grandmother(p1, p2):
    return False

# -- Return True is p1 is a maternal ancestor of p2
#    That is, if p1 is p2's mother, or p2's mother's mother, etc.
def is_maternal_ancestor(p1, p2):
    return False

# -- Return True if p1 is an ancestor of p2
#    On either side of the family tree
def is_ancestor(p1, p2):
    return False

# ---- Main program ------------------------------------------------

fn = input('Enter family tree file name: ')
people = read_family_file(fn)
print('Found {} people'.format(len(people)))

s = find_person('Sam', people)
j = find_person('Jane', people)
if is_mother(j, s):
    print('Yes')
else:
    print('No')

# --- Add more test cases here ------