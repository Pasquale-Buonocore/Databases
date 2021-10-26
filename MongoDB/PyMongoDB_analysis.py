import pymongo
from pymongo import MongoClient # Oggetto che permette di connettersi al DB

# Connessione al DB
client = MongoClient('localhost', 27017)

# Let's find all the database in that client
AllDatabesName = client.database_names()
# Carico il database delle Deadlines
if "DeadlinesBoard" in AllDatabesName:
    DeadLinesBoard = client.DeadlinesBoard

DeadLinesBoard_collection = DeadLinesBoard.list_collection_names()
if "persone" in DeadLinesBoard_collection:
    # Accedo alla collection persone
    persone_coll = DeadLinesBoard.persone

# Find the number of people whose name is Pasquale
persone_coll.count_documents({"nome":"Pasquale"})

