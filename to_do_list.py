# Mini Projet : To Do list -------------------------------------------------------------

print("Bienvenue dans votre To Do List !")

taches = []

def menu():
    print("\n----To Do List ----")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Quitter")

def ajouter_tache():
    nb_taches = int(input("\nCombien de tâches voulez-vous ajouter ? : " ))
    for _ in range(nb_taches):  
        tache = input("Entrez votre tâche : ")
        taches.append(tache)
        print(f"\nLa tache '{tache}' a été ajoutée à votre To Do List")
        print(taches, "\n")

def merci():
    print("\nA bientot dans votre To Do List !")


while True:
    menu()
    
    choix = input ("\nQuelle est votre choix ? : ")
    match choix :
        case "1" :
            ajouter_tache()
        case "2" :
            pass
        case "3" :
            pass
        case "4" :
            merci()
            break
        case _ :
            print("\nChoix invalide ! Veuillez réesayer.") 