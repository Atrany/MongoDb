import sys
import cursor

from random import randint

print("====================")
print("|       MENU       |")
print("====================")

print("Bonjour et bienvenue sur l'interface de gestion immobilière. Tout d'abord, veuillez sélectionnez la catégorie que vous souhaitez traiter : ")
print("1 : les agences.")
print("2 : les propriétaires.")
print("3 : les locataires.")
print("4 : Aucune de ces propositions, ils me conviennent comme ils sont actuellement.")
reponse = input("Votre choix : ")

if reponse == "1":
    print("Vous avez donc choisis les agences. Voici les différentes options à votre disposition : ")
    print("1 : Créer une nouvelle agence.")
    print("2 : Voir les agences déjà crées.")
    print("3 : Modifier une agence crée.")
    print("4 : Supprimer une agence existante.")
    print("5 : Aucune des options précédentes.")
    reponseagence = input("Votre choix : ")

    if reponseagence == "1":
        print("Vous avez choisi de créer une nouvelle agence. Voici les informations que vous devrez rentrer : ")

        nom = input("Le nom de votre agence : ")
        adresse = input("L'adresse de votre agence (Numéro et nom de rue, code postal - ville) : ")
        numero = input("Le numéro de votre agence : ")

        from pymongo import MongoClient

        client = MongoClient('localhost', 27017, username='agenceAdm', password='root', authSource='agences', authMechanism='SCRAM-SHA-256')
        db = client.agences

        for x in (1, 1):
            agence = {
                'Nom': nom,
                'Adresse': adresse,
                'Numero': numero,
                'Note': randint(1, 5)
            }
        print(agence)
        print('Création de votre agence réussie !')

    elif reponseagence == "2":
        print("Vous avez choisi de voir les agences déjà crées. Les voici : ")
        from pymongo import MongoClient

        client = MongoClient('localhost', 27017, username='agenceAdm', password='root', authSource='agences',authMechanism='SCRAM-SHA-256')
        db = client.agences

        listagence = db.agences
        selectagence = list(listagence.find())

        print(selectagence)
        print("Voici toutes les agences crées.")

        fivestarcount = db.agences.find({'Note': 5}).count()

        print("Voici le nombre d'agences ayant une note de 5 : "+str(fivestarcount))

        # findlogement = db.agences.aggregate()
    elif reponseagence == "3":
        print("Vous avez choisi de modifier une agence crée.")
        print("Veuillez entrer ce que vous souhaitez modifier dans cette agence : ")
        print("1: Le nom")
        print("2: L'adresse")
        print("3: Le numéro")
        choixmodifagence = input("Votre choix : ")

        if choixmodifagence == "1":

            from pymongo import MongoClient

            from pprint import pprint

            client = MongoClient('localhost', 27017, username='agenceAdm', password='root', authSource='agences', authMechanism='SCRAM-SHA-256')
            db = client.agences

            ASingleAgence = db.agences.find_one({'Nom': "Lebuisson"})

            resultat = db.agences.update_one({'_id': ASingleAgence.get('_id')}, {'$set': {'Nom': "La Forêt"}})

            UpdatedDocument = db.agences.find_one({'_id': ASingleAgence.get('_id')})
            print('Votre agence mise à jour : ')
            pprint(UpdatedDocument)

        elif choixmodifagence == "2":

            from pymongo import MongoClient

            from pprint import pprint

            client = MongoClient('localhost', 27017, username='agenceAdm', password='root', authSource='agences',
                                 authMechanism='SCRAM-SHA-256')
            db = client.agences

            ASingleAgence = db.agences.find_one({'Nom': "Century22"})

            resultat = db.agences.update_one({'_ id': ASingleAgence.get('_ id')}, {'$set': {'Adresse': "45 avenue Alfred Hitchcock, 62000 - Dainville"}})

            UpdatedDocument = db.agences.find_one({'_ id': ASingleAgence.get('_ id')})
            print('Votre agence mise à jour:')
            pprint(UpdatedDocument)

        elif choixmodifagence == "3":

            from pymongo import MongoClient

            from pprint import pprint

            print("Veuillez entrez le nom de l'agence a modifier : ")
            nomagence = input("Le nom de l'agence a modifier : ")
            print("Avant toute chose, veuillez entrer le numéro modifié de l'agence : ")
            numeromodifagence = input("Le numéro modifié : ")

            client = MongoClient('localhost', 27017, username='agenceAdm', password='root', authSource='agences',
                                 authMechanism='SCRAM-SHA-256')
            db = client.agences

            ASingleAgence = db.agences.find_one({'Nom': "AgenceImmo"})

            resultat = db.agences.update_one({'_ id': ASingleAgence.get('_ id')}, {'$set': {'Numéro': "0347200001"}})

            UpdatedDocument = db.agences.find_one({'_ id': ASingleAgence.get('_ id')})
            print('Votre agence mise à jour :')
            pprint(UpdatedDocument)

        else:
            print("Je ne comprend pas votre choix. Veuillez réessayer.")
            choixmodifagence = input("Votre choix : ")

    elif reponseagence == "4":
        print("Vous avez choisi de supprimer une agence existante. Veuillez entrez le nom de l'agence a supprimer : ")
        agencesupp = input("Le nom :")

        from pymongo import MongoClient

        client = MongoClient('localhost', 27017, username='agenceAdm', password='root', authSource='agences',
                             authMechanism='SCRAM-SHA-256')
        db = client.agences

        result = db.agences.delete_many({"Nom": agencesupp})

        print("L'agence sélectionné a bien été supprimé.")

    elif reponseagence == "5":
        print("Je vais donc arrêter le programme. Bonne journée ! :) ")
        sys.exit()
    else:
        print("Je ne connais pas cette action. Veuillez refaire un choix : ")
        reponseagence = input("Votre choix : ")

elif reponse == "2":
    print("Vous avez donc choisis les propriétaires. Voici les différentes options à votre disposition : ")
    print("1 : Créer un nouveau propriétaire.")
    print("2 : Voir les propriétaires déjà crées.")
    print("3 : Modifier un propriétaire crée.")
    print("4 : Supprimer un propriétaire existant.")
    print("5 : Aucune des options précédentes.")
    reponseproprietaire = input("Votre choix : ")
    if reponseproprietaire == "1":

        from pymongo import MongoClient

        client = MongoClient('localhost', 27017, username='proprietaireAdm', password='root', authSource='proprietaire',
                             authMechanism='SCRAM-SHA-256')
        db = client.proprietaire

        nom = input("Veuillez entrez le nom du propriétaire : ")
        adresse = input("Veuillez entrez l'adresse du propriétaire : ")
        numero = input("Veuillez entrez le numéro du propriétaire : ")
        logeadresse = input("Veuillez entrez l'adresse du logement de la location : ")
        logeprix = input("Veuillez entrez le prix de la location : ")
        logeville = input("Veuillez entrez la ville de la location : ")
        logeloc = input("Veuillez entrez si le logement est loué ou non (Loué/Non loué) : ")

        for x in (1, 1):
            proprietaire = {
                'Nom': nom,
                'Adresse': adresse,
                'Numero': str(numero),
                'Logement': [{'Adresse': logeadresse,
                              'Prix': logeprix,
                              'Ville': logeville,
                              'Location': logeloc}]
            }
        resultat = db.proprietaire.insert_one(proprietaire)
        print(proprietaire)
        print('Création du propriétaire réussie !')
    elif reponseproprietaire == "2":
        from pymongo import MongoClient

        client = MongoClient('localhost', 27017, username='proprietaireAdm', password='root', authSource='proprietaire',
                             authMechanism='SCRAM-SHA-256')
        db = client.proprietaire

        listproprio = db.proprietaire
        selectproprio = list(listproprio.find())

        print(selectproprio)
        print("Voici la liste des propriétaires.")
        
    elif reponseproprietaire == "3":
        from pymongo import MongoClient

        from pprint import pprint

        client = MongoClient('localhost', 27017, username='proprietaireAdm', password='root', authSource='proprietaire',
                             authMechanism='SCRAM-SHA-256')
        db = client.proprietaire

        ASingleProprietaire = db.proprietaire.find_one({'Nom': 'Jean-Jacques FAUCHE'})

        resultat = db.proprietaire.update_one({'_ id': ASingleProprietaire.get('_ id')},
                                              {'$set': {'Nom': 'Jean DUJARDIN'}})

        UpdatedDocument = db.proprietaire.find_one({'_ id': ASingleProprietaire.get('_ id')})
        print('Le propriétaire mis à jour:')
        pprint(UpdatedDocument)

    elif reponseproprietaire == "4":
        print("Veuillez entrez le nom du propriétaire à supprimer : ")
        nomproprio = input("Le nom : ")
        from pymongo import MongoClient

        client = MongoClient('localhost', 27017, username='proprietaireAdm', password='root', authSource='proprietaire',
                             authMechanism='SCRAM-SHA-256')
        db = client.proprietaire
        result = db.proprietaire.delete_many({"Nom": nomproprio})

        print(result)
        print("Le proprétaire a été supprimé.")
    elif reponseproprietaire == "5":
        print("Nous allons donc arrêter le programme. Bonne journée ! :)")
        sys.exit()
    else:
        print("Je ne connais pas cette action. Veuillez recommencer : ")
        reponseproprietaire = input("Votre choix : ")
elif reponse == "3":
    print("Vous avez donc choisis les locataires. Voici les différentes options à votre disposition : ")
    print("1 : Voir les locataires déjà crées.")
    print("2 : Modifier un locataire crée.")
    print("3 : Aucune des options précédentes.")
    reponselocataire = input("Votre choix : ")
    if reponselocataire == "1":
        print("Voici la liste des locataires : ")
        from pymongo import MongoClient

        client = MongoClient('localhost', 27017, username='locataireAdm', password='root', authSource='locataire',
                             authMechanism='SCRAM-SHA-256')
        db = client.locataire

        listlocataire = db.locataire
        selectlocataire = list(listlocataire.find())
        print(selectlocataire)

    elif reponselocataire == "2":
        print(" Voici la modification du nom d'un locataire : ")
        from pymongo import MongoClient

        from pprint import pprint

        client = MongoClient('localhost', 27017, username='locataireAdm', password='root', authSource='locataire',
                             authMechanism='SCRAM-SHA-256')
        db = client.locataire

        ASingleLocataire = db.locataire.find_one({'Nom': 'Jean DUCHAMPS'})
        print('Un exemple de document:')
        pprint(ASingleLocataire)

        resultat = db.locataire.update_one({'_ id': ASingleLocataire.get('_ id')}, {'$set': {'Nom': 'Thomas DUBOIS'}})

        UpdatedDocument = db.locataire.find_one({'_ id': ASingleLocataire.get('_ id')})
        print('Le document mis à jour:')
        pprint(UpdatedDocument)

    elif reponselocataire == "3":
        print("Nous allons donc arrêter le programme. Bonne journée ! :)")
        sys.exit()
elif reponse == "4":
    print("Nous allons donc arrêter le programme. Merci à vous et bonne journée ! :) ")
    sys.exit()
else:
    print("Je ne connais pas cette action. Nous allons donc arrêter le programme par défaut. Bonne journée à vous ! :)")
    sys.exit()