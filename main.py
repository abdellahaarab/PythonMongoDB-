
from logic import GST

def Welcome():
    print("""
        ************Geste ......... **********
        1 ----- Ajouter 
        2 ----- Afficher
        3 ----- Afficher p Vile D 
        4 ----- Sup p Nom
        5 ----- Sauvgarder 
        6 ----- Afficher Min
        *****************************************
    """)
    



while True:
    print('------------------------------------------------')
    Welcome()
    choix = int(input("Votre choix :"))
    if choix == 1:
        tb = {}
        tb['nom'] = input("Nome : ")
        tb['dist'] = int(input("Distance : "))
        tb['viled'] = input("Vile D : ")
        tb['vileA'] = input("Vile A : ")
        GST.Ajouter(GST,tb)
    if choix == 2:
        GST.__str__(GST)
        
    if choix == 3:
        tb = input("Vile D : ")
        print(GST.rechercher(GST,tb))
    if choix == 4:
        Nom = input("Nom : ")
        print(GST.suprimer(GST,Nom))

    if choix == 5:
        Nom = input("Nom : ")
        GST.sof(GST,Nom)
           
    if choix == 6:
        print(GST.ShortRout(GST))
              
              
    print('Pour Quitter ctrl + C')
    print('------------------------------------------------')
        
            