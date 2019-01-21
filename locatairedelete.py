from random import randint

from pymongo import MongoClient

from pprint import pprint

client = MongoClient('localhost', 27017, username='locataireAdm', password='root', authSource='locataire', authMechanism='SCRAM-SHA-256')
db = client.locataire
#serverStatusResult = db.command("serverStatus")
#pprint(serverStatusResult)

result = db.locataire.delete_many ({"Nom": "Jean DUCHAMPS"})

