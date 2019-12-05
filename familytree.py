
# A person is a tuple of a name and two parents

p0 = ('unknown', None, None)
p1 = ('Samuel', p0, p0)
p2 = ('Nora', p0, p0)
p3 = ('Isabel', p1, p2)
p4 = ('James', p0, p0)
p5 = ('Ethel', p0, p0)
p6 = ('Jim', p4, p5)
p7 = ('Jane', p6, p3)
p8 = ('Peter', p6, p3)
p9 = ('Liza', p6, p3)
p10 = ('Tim', p6, p3)
p11 = ('Manny', p0, p0)
p12 = ('Elsa', p0, p0)
p13 = ('Channa', p11, p12)
p14 = ('Irving', p0, p0)
p15 = ('Ida', p0, p0)
p16 = ('Sydney', p14, p15)
p17 = ('Bernard', p16, p13)
p18 = ('Marilyn', p16, p13)
p19 = ('Evelyn', p16, p13)
p20 = ('Sam', p17, p7)
p21 = ('Nathan', p17, p7)
p22 = ('Kate', p17, p7)
p23 = ('Sid', p0, p0)
p24 = ('Adrianna', p0, p0)
p25 = ('Ellyn', p23, p24)
p26 = ('Bert', p0, p0)
p27 = ('Marcy', p0, p0)
p28 = ('Stephen', p26, p27)
p29 = ('Aliza', p28, p25)
p30 = ('David', p28, p25)
p31 = ('Michael', p28, p25)
p32 = ('Jonah', p20, p29)
p33 = ('Nella', p0, p0)
p34 = ('Jacob', p30, p33)
p35 = ('Jonathan', p30, p33)
p36 = ('Hanna', p30, p33)
p37 = ('Amanda', p0, p0)
p38 = ('Hannah', p21, p37)
p39 = ('Owen', p21, p37)
p40 = ('Bill', p0, p0)
p41 = ('William', p40, p22)
p42 = ('Grace', p40, p22)

everyone = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10,
            p11, p12, p13, p14, p15, p16, p17, p18, p19, p20,
            p21, p22, p23, p24, p25, p26, p27, p28, p29, p30,
            p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42]

def lookup(name, people):
    for p in people:
        if name == p[0]:
            return p
    return None

def is_parent(parent, child):
    return False

def are_siblings(child1, child2):
    return False

def are_cousins(c1, c2):
    return False


def all_children(parent, people):
    return

def all_cousins(person, people):
    return


# ---- Program starts here ---------------------------


