# difference

setA = set((1,2,3,4,5)) # We defined set as setA.

setB = set((1,3,4,6,7,8)) # We defined set as setB.

print(setA - setB) # We printed the elements of A that are different from B.

print(setA.difference(setB)) # We printed the elements of A that are different from B.

# symetric difference

print(setA ^ setB) # We printed elements of A that are different fromB or elements of B that are different from A.

print(setA.symmetric_difference(setB)) # We printed elements of A that are different fromB or elements of B that are different from A.