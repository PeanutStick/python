from random import randint
x = 1
while  x == 1 :
    #crée un nombre
    nb = (randint(0, 100))
    tentative = int(input('choisis le nombre de tentative : '))
    #initialisation du compteur
    i = 0
    #l'utilisateur choisi un nombre

    while i < tentative :
        decompte = str(tentative-i)
        choix = int(input(decompte +' chances restante !!!choisis un nombre entre 0 et 100 : '))
        

        if choix > nb :
            print('trop grand')
            i += 1
            #print(tentative-i)
        elif choix < nb :
            print('trop petit')
            i += 1
            #print(tentative-i)
        else:
            print('GG')
            i = tentative + 1
            break

    r = input('continuer ? Oui ou Non :')
    if r == "O" : 
        x = 1
    else :
        x =0
        print("a+")
    
