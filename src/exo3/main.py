def interface(page):
    print(" ")
    print(f"---- {page} ----")
    print(" ")   

def error_connection():
    print("Vous devez être connecté pour utiliser cette commande !")    

def error_permission():
    print("Oups, vous n'avez pas la permission d'utiliser cette commande !")

def exercice3():
    accounts = {"Administrateur": "admin"}
    tasks = dict()
    
    online_user = ""
    
    while True:
        interface("ManageMySpaceship")
        if online_user == "":
            print("/!\ Aucun utilisateur connecté")
            command = input("Entrez une commande : ")
        else:
            command = input(f"({online_user}) Entrez une commande : ")
        
        if command.lower() == "connecter":
            interface("Connexion")
            name = input("Nom : ")
            if name in accounts.keys():
                online_user = name
                print(f"Vous êtes à présent connecté en tant que {online_user} !")
            else:
                print("utilisateur introuvable !")
                 
        elif command.lower() == "ajouter-compte":
            if online_user != "":
                if accounts[online_user] == "admin":
                    interface("Ajouter un utilisateur")
                    name = input("Nom : ")
                    permission = input("permission administrateur (oui/non) : ")
                    if permission == "oui" or permission == "o":
                        accounts[name] = "admin"  
                    else:
                        accounts[name] = "user"
                    print(f"L'utilisateur {name} a été ajouté avec les droits {accounts[name]} !")
                else:
                    error_permission()
            else:
                error_connection()
                
        elif command.lower() == "supprimer-compte":
            if online_user != "":
                if accounts[online_user] == "admin":
                    interface("Supprimer un utilisateur")
                    name = input("Nom : ")
                    if name in accounts.keys():
                        if name != online_user:
                          accounts.pop(name)
                          print(f"L'utilisateur {name} a été supprimé !")
                        else:
                          print("Eh oh ! Ne supprime pas ton compte !")
                    else:
                        print(f"L'utilisateur {name} n'existe pas !")
                else:
                    error_permission()
            else:
                error_connection()
            
        elif command.lower() == "ajouter":
            if online_user != "":
                interface("Ajouter une tâche")
                name = input("Nom : ")
                description = input("Description : ")
                users = list()
                while True:
                    user = input("Entrez les assignés (laisser vide pour finir) : ")
                    if len(user) == 0:
                        break
                    else:
                        if user in accounts.keys():
                            users.append(user)
                            print(f"{user} ajouté !")
                        else:
                            print(f"L'utilisateur {user} n'existe pas !")
                tasks[name] = [description, users, ""]
                print(f"la tâche {name} ({description}) a été ajouté !")
            else:
                error_connection()
            
        elif command.lower() == "retirer":
            if online_user != "":
                if accounts[online_user] == "admin":
                    interface("Retirer une tâche")
                    name = input("Nom : ")
                    if name in tasks.keys():
                        tasks.pop(name)
                        print(f"La tâche {name} e été retiré !")
                    else:
                        print(f"La tâche {name} n'exite pas !")
                else:
                    error_permission()
            else:
                error_connection()
        
        elif command.lower() == "compléter":
            if online_user != "":
                interface("Compléter une tâche")
                name = input("Nom : ")
                if name in tasks.keys():
                    if online_user in tasks[name][1] or accounts[online_user] == "admin":
                        tasks[name][2] = online_user
                        print(f"La tâche {name} a été complété !")
                    else:
                        print("Vous ne pouvez pas compléter cette tâche !")
                else:
                    print("Cette tâche n'existe pas !")
            else:
                error_connection()
                
        elif command.lower() == "liste":
            if online_user != "":
                number = 1
                interface("Liste")
                if accounts[online_user] == "admin":
                    for tache in tasks:
                        statut = "Non" if tasks[tache][2] == "" else tasks[tache][2]
                        print(f"{number}.\nNom : {tache}\nDescription : {tasks[tache][0]}\nComplété : {statut}\n ")
                        number += 1
                else:
                    for tache in tasks:
                        if online_user in tasks[tache][1]:
                            statut = "Non" if tasks[tache][2] == "" else "Oui"
                            print(f"{number}.\nNom : {tache}\nDescription : {tasks[tache][0]}\nComplété : {statut} \n ")
                            number += 1
            else:
                error_connection()
        
        elif command.lower() == "vider":
            if online_user != "":
                if accounts[online_user] == "admin":
                    interface("vider les tâches")
                    tasks.clear()
                    print("Les tâches ont été vidées !")
                else:
                    error_permission()
            else:
                error_connection()
                
        else:
            print("Oups, commande introuvable !")