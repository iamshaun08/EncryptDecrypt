import E
import numpy as np

inv = np.linalg.inv(E.matrix())

#def decrypt():
#    e = E.encrypt()
#    decipher_mat = []
#    for i in range(len(e[1])):
#        decipher_mat.append(e[1][i]*inv)
#    decipher_mat = np.round(decipher_mat)
#    decipher_list = []
#    for i in range(len(decipher_mat)):
#        for j in range(len(decipher_mat[i])):
#            for k in range(len(decipher_mat[i][j])):
#                decipher_list.append(int(decipher_mat[i][j][k]))
#    decipher = ''
#    for i in decipher_list:
#        decipher += alph()[i]
#    return (e[0],decipher)

def alph():
    alph = E.alph
    return alph

def decrypt():
    e = E.encrypt()
    cipher_list = []
    for i in e[0]:
        cipher_list.append(alph().index(i) + (e[2][e[0]].index(e[0][i])*len(alph())-1))
    mat_list = []
    for i in range(0,len(cipher_list),2):
        mat_list.append(cipher_list[i:i+2])
    decipher_mat = []
    for i in range(len(mat_list)):
        decipher_mat.append(mat_list[i]*inv)
    decipher_mat = np.round(decipher_mat)
    decipher_list = []
    for i in range(len(decipher_mat)):
        for j in range(len(decipher_mat[i])):
            for k in range(len(decipher_mat[i][j])):
                decipher_list.append(int(decipher_mat[i][j][k]))
    decipher = ''
    for i in decipher_list:
        decipher += alph()[i]
    return (e[0],decipher)