import numpy as np

a = np.matrix("1 2;3 4")
b = np.linalg.inv(a)
l = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
l1 = []

s2 = input("Enter message: ")
s = s2.lower()
if len(s)%2:
    s += " "
else:
    pass
print(s)
for i in s:
    l1.append(l.index(i))
#print(l1)
l2 = []

for i in range(0,len(l1),2):
    l2.append(l1[i:i+2])
#print(l2)
l7 = []

for i in range(len(l2)):
   l7.append(l2[i]*a)


l3 = np.round(l7)
#print(l3)
l8 = []

for i in range(len(l3)):
    for j in range(len(l3[i])):
        for k in range(len(l3[i][j])):
            l8.append(l3[i][j][k])
print(l8)

l9 = []

for i in range(len(l8)):
    x = l8[i]//26
    if x:
        l9.append(l8[i]-(x*26))
    else:
        l9.append(l8[i])
print(l9)        
cipher = ''

for i in l9:
    h = int(i)
    cipher += l[h]
print(cipher)

l4 = []
for i in range(len(l3)):
    l4.append((l3[i]*b))
#print(l4)

l5 = np.round(l4)
#print(l5) 
l6 = []

for i in range(len(l5)):
    for j in range(len(l5[i])):
        for k in range(len(l5[i][j])):
            l6.append(l5[i][j][k])
#print(l6)
s2 = ''
for i in l6:
    h = int(i)
    s2 += l[h]

print(s2)