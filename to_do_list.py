# Mini Projet : To Do list -------------------------------------------------------------

def menu():
    print("\n----------------------To Do List ------------------------------")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Quitter")


def ajouter_tache(taches):
    nb_taches = int(input("\nCombien de tâches voulez-vous ajouter ? : " ))
    
    if nb_taches > 0:
        for _ in range(nb_taches):  
            tache = input("\nEntrez votre tâche : ")
            taches.append(tache)
            print(f"La tache '{tache}' a été ajoutée à votre To Do List")
    else:
        print("Le nombre de tâches à ajouter doit être supérieur à 0 ! Veuillez réesayer.")


def montrer_tache(taches):
    if taches:
        print("\nVoici votre To Do List ----------------------------------------\n")
        for i, tache in enumerate(taches, start=1):
            print(f"{i}. {tache}")
    else:
        print("\nVotre To Do List est vide !")


def supprimer_tache(taches):
    montrer_tache(taches)
    numero_tache = int(input("\nEntrez le numéro de la tâche à supprimer : "))
    if numero_tache > 0 and numero_tache <= len(taches):
        tache_supprimer = taches.pop(numero_tache - 1)
        print(f"La tache '{tache_supprimer}' a été supprimée de votre To Do List")
    else:
        print("\nNuméro de tâche invalide ! Veuillez réesayer.")


def merci():  
    print("\nA bientôt dans votre To Do List !")


def main():
    taches = []
    while True:
        menu()

        choix = input("\nQuelle est votre choix ? : ")
        match choix:
            case "1" :
                ajouter_tache(taches)
            case "2" :
                montrer_tache(taches)
            case "3" :
                supprimer_tache(taches)
            case "4" :
                merci()
                break
            case _ :
                print("\nChoix invalide ! Veuillez réesayer.")
                
if __name__ == "__main__":
    main()