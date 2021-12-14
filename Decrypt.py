import Encrypt
import numpy as np

alph = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

inv = np.linalg.inv(Encrypt.matrix())

def decrypt():
    e = Encrypt.encrypt()
    decipher_mat = []
    for i in range(len(e[1])):
        decipher_mat.append(e[1][i]*inv)
    decipher_mat = np.round(decipher_mat)
    decipher_list = []
    for i in range(len(decipher_mat)):
        for j in range(len(decipher_mat[i])):
            for k in range(len(decipher_mat[i][j])):
                decipher_list.append(int(decipher_mat[i][j][k]))
    decipher = ''
    for i in decipher_list:
        decipher += alph[i]
    return (e[0],decipher)

