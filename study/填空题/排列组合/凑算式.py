from itertools import permutations,combinations

c=0
for n in permutations(range(1,10)):
    A,B,C,D,E,F,G,H,I = n
    DEF =100*D+10*E+F
    GHI =100*G+10*H+I

    if A * C * GHI + B * GHI + DEF * C == 10 * C * GHI:
        c+=1
print(c)
