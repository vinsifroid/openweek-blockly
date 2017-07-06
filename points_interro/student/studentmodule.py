#!/bin/python3
# Code to be verified

#    This file is part of INGInious.
#    Copyright (C) 2017, Duchêne François et Raquet Damien
points_interro = 12
a_moins_10 = False
a_entre_10_et_16 = False
a_plus_16 = False

'''
    @pre p != None
    @post met les points_interro à p et les conditions à false
'''
def set_cond_test(p):
    global points_interro, a_moins_10, a_entre_10_et_16, a_plus_16
    points_interro = p
    a_moins_10 = False
    a_entre_10_et_16 = False
    a_plus_16 = False

def donner_glace():
    global a_plus_16
    a_plus_16 = True

def confisquer():
    global a_moins_10
    a_moins_10 = True

def maman_contente():
    global a_entre_10_et_16
    a_entre_10_et_16 = True

def point():
    global points_interro
    return points_interro

def student_code():
@    @interro@@
    return {"a_moins_10": a_moins_10, "a_entre_10_et_16": a_entre_10_et_16, "a_plus_16": a_plus_16}

if __name__ == "__main__":
    pass_test = True
    # On teste sur les 20 valeurs possibles
    for i in range(0,21):
        set_cond_test(i)
        ret = student_code()
        #Trois cas possibles, michel a eu - de 10, l'étudiant a eu entre 10 et 16 et l'étudiant a + de 16
        #Une seule des conditions ne peut être True
        if ret == {"a_moins_10": True, "a_entre_10_et_16": False, "a_plus_16": False} and points_interro < 10:
            pass
        elif ret == {"a_moins_10": False, "a_entre_10_et_16": True, "a_plus_16": False} and points_interro < 17 and 9 < points_interro :
            pass
        elif ret == {"a_moins_10": False, "a_entre_10_et_16": False, "a_plus_16": True} and 16 < points_interro:
            pass
        else:
            #si un test échoue, on ne print pas True
            pass_test=False
            print('Ton programme ne fonctionne si Michel a eu ' + str(i) + "\n")
    if pass_test:
        print('True')
