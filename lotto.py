#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from random import*
aleatoire=randint(1,99)
jeu=[0]*3
jeu_liste=[]
etape=0
depart=1
victoire=[]
gain=[] 
liste=""
choix="""
*********************************************
***********BIENVENUE À NAN-LOTTO***********
*********************************************
	Tapez :
        1/pour enregistrer un pari
        2/pour afficher les pari enregistrés
        3/ pour voir le resultat : 
   """
while etape!=3:
    if etape==1:
        print(" Pari N° "+str(depart)+" : ")
        jeu[0]=input("Entrez le nom du joueur  "+str(depart)+" :\n ")
        jeu[1]=int(input("Entrez le numéro choisi entre 1 et 99 :\n "))
        jeu[2]=int(input("Entrez le montant de la mise :\n "))
        jeu_liste.append(jeu)
        jeu=[0]*3
        depart+=1
    elif etape==2:
        if len(jeu_liste)!=0:
            for i in range(len(jeu_liste)):
                print(jeu_liste[i][0]+" " +"a parié sur le numéro " +" " +str(jeu_liste[i][1]) +" " +"et a misé la somme de  "+" " +str(jeu_liste[i][2])	+"\n" )
        else:
            print("Aucun pari enregistré pour le moment  ! ")
    etape=int(input(choix))
for i in range(len(jeu_liste)):
    if jeu_liste[i][1]==aleatoire:
        victoire.append(jeu_liste[i][0])
        gain.append((jeu_liste[i][2])*50)
if len(victoire)!=0:
    for i in range(len(victoire)):
        liste+=victoire[i] +" \n" 
    for i in range(len(gain)) :
        liste2+=gain[i] + "\n" 
    choix="le numéro gagnant est "+str(aleatoire)+" les gagnants sont :\n "+liste +" " +" "  "et ils gagne respectivement : \n" +liste2
else:
    choix="le numéro gagnant était "+str(aleatoire)+" Dommage ! Il n'y a aucun gagnant "
print(choix)
