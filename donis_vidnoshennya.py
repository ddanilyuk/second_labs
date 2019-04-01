import random

def a_mother_b(A, B, women_1):
    womenset_1 = set()
    for i in A:
        if i in women_1:
            womenset_1.add(i)
    womenset_2 = set()
    for i in B:
        if i in women_1:
            womenset_2.add(i)
    S = []
    for i in range(min(len(womenset_1), len(womenset_2))):
        m = random.choice(list(womenset_1))
        w = random.choice(list(womenset_2))
        if m != w:
            S.append([m, w])
            womenset_1.remove(m)
            womenset_2.remove(w)

    return S


# нужно поменять!!!!!!!!
def a_universal_father_in_law_b(A, B, mens):
    mensetA = set()
    for i in A:
        if i in mens:
            mensetA.add(i)
    mensetB = set()
    for i in B:
        if i in mens:
            mensetB.add(i)
    # Ur=list(map(lambda x: x * , mile_distances))
    Ur = []
    for m1 in mensetA:
        for m2 in mensetB:
            if m1 != m2:
                Ur.append([m1, m2])
    return Ur


# print(a_husbend_b())
# print(a_father_in_law_b())
"""
Ur = list(a_universal_father_in_law_b())
print("Ur > ", a_universal_father_in_law_b())
S = list(a_husbend_b())
print(S)
R = list(a_father_in_law_b())
print(R)

"""
def unionn(s, r):
    U = []
    for i in s:
        U.append(i)
    for i in r:
        if i not in U:
            U.append(i)
    return U


#print(unionn(R, S))


# print(S)
# print(R)

def intersectionn(s, r):
    I = []
    for i in s:
        # print(i if i in s else "0")
        if i in r:
            I.append(i)
    return I


#print(intersectionn(R, S))


def differ(r, s):
    D = []
    for i in r:
        if i not in s:
            D.append(i)
    return D


#print(differ(R, S))


def transposed(s):
    T = []
    for i in range(len(s)):
        T.append([s[i][1], s[i][0]])
    return T


#print(transposed(S))
#5print(differ(Ur, R))
