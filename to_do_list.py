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
        tache = input("\nEntrez votre tâche : ")
        taches.append(tache)
        print(f"La tache '{tache}' a été ajoutée à votre To Do List")

def montrer_tache():
    print("\nVoici votre To Do List : ")
    for i, tache in enumerate(taches, start=1):
        print(f"{i}. {tache}")


def supprimer_tache():
    montrer_tache()
    numero_tache = int(input("\nEntrez le numéro de la tâche à supprimer : "))
    if numero_tache > 0 and numero_tache <= len(taches):
        tache_supprimer = taches.pop(numero_tache - 1)
        print(f"La tache '{tache_supprimer}' a été supprimée de votre To Do List")


def merci():  
    print("\nA bientôt dans votre To Do List !")


while True:
    menu()
    
    choix = input ("\nQuelle est votre choix ? : ")
    match choix :
        case "1" :
            ajouter_tache()
        case "2" :
            montrer_tache()
        case "3" :
            supprimer_tache()
        case "4" :
            merci()
            break
        case _ :
            print("\nChoix invalide ! Veuillez réesayer.") 