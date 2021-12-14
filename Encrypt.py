import numpy as np

def matrix():
    mat = np.matrix("7 4;5 3")
    return mat

mat = matrix()

alph = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    
def inp():
    s = input("Enter message: ")
    s.lower()
    for i in s:
        if i in alph:
            pass
        else:
            print("Enter alphanum only: ")
            inp()
    if len(s)%2:
        s += " "
    else:
        pass
    return s

#s = inp()
#print(s)

def msg_to_mat():
    s = inp()
    alph_list = []
    for i in s:
        alph_list.append(alph.index(i))
    mat_list = []
    for i in range(0,len(alph_list),2):
        mat_list.append(alph_list[i:i+2])
    return mat_list

#msg_to_mat = msg_to_mat()
#print(msg_to_mat)

def encrypt():
    mat_list = msg_to_mat()
    cipher_mat = []
    for i in range(len(mat_list)):
        cipher_mat.append(mat_list[i]*mat)
    cipher_mat = np.round(cipher_mat)
    cipher_list = []
    for i in range(len(cipher_mat)):
        for j in range(len(cipher_mat[i])):
            for k in range(len(cipher_mat[i][j])):
                cipher_list.append(cipher_mat[i][j][k]) 
    cipher = ''
    for i in cipher_list:
        x = i//(len(alph)-1)
        if x:
            cipher += alph[i-x*(len(alph)-1)]
        else:
            cipher += alph[i]
    return (cipher,cipher_mat)
