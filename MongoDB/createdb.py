import pymongo
from pymongo import MongoClient # Oggetto che permette di connettersi al DB

# Connessione al DB
client = MongoClient('localhost', 27017)

# Creo un database
db = client.DeadlinesBoard

# Creo una collection
persone_coll = db.persone

# Creo una serie di indici (per velocizzare l'accesso ai dati in seguito)
persone_coll.create_index([("nome",pymongo.ASCENDING)])
persone_coll.create_index([("cognome",pymongo.ASCENDING)])
persone_coll.create_index([("computer",pymongo.ASCENDING)])

# Creo un documento di tipo BSON usando la forma utilizzata un DICT
p1 = {"nome":"Pasquale","cognome":"Buonocore","età":27,"computer":["MSI","APPLE"]}
p2 = {"nome":"Giuseppe","cognome":"Buonocore","età":47,"computer":["MSI","APPLE"]}

# Inserire il documento nella collection
persone_coll.insert_one(p1)
persone_coll.insert_one(p2)


print('ciao')

