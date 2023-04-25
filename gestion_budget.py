import sqlite3

print("Application de Gestion de budget avec Python et Sqlite3")
with sqlite3.connect("budget.db") as connection:
    cursor = connection.cursor()

        
    def le_revenu():
        somme_revenu=float(input("donnez la somme obtenu de votre revenu:"))
        print(somme_revenu)
        return somme_revenu
    le_revenu()
    
    def la_depense(somme_revenu, somme_depensé): 
        somme_dépensé=float(input("donnez la somme dépensé de votre dépense:"))
        print(somme_dépensé)
        if somme_revenu > somme_dépensé:
            somme_revenu=somme_revenu - somme_dépensé
            print("l'ecart qui existe entre les deux est:",somme_revenu)
        else:
            print("votre solde est insuffissant") 
        return somme_revenu, somme_depensé
    la_depense(1, 1)        