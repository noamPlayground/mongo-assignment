import pymongo
from bson.json_util import dumps
from helpers import getDataFileListOfDicts

EXPORT_PATH = "exportData/users.json"


def initMongoClient():
    # Establishes connection with MongoDB and returns client

    try:
        myclient = pymongo.MongoClient("mongodb://mongo:27017/")
        return myclient
    except Exception as e:
        return f"Could on connect to Mongo DB. Exception: {e}"


def createDbInMongo(myclient):
    # Creates db in MongoDB and returns it
    # args: myclient - MongoDB client

    mydb = myclient["cr-db"]
    return mydb


def createCollectionInMongo(myclient, mydb):
    # Creates collection in MongoDB and returns it
    # args: myclient - MongoDB client, mydb - mongoDB db object

    mycol = mydb["users"]
    return mycol


def insertDataFileIntoMongoCollection(myclient, collection):
    # inserts data file into given MongoDB collection
    # args: myclient - MongoDB client, collection - MongoDB collection

    data = getDataFileListOfDicts()
    collection.insert_many(data)
    dblist = myclient.list_database_names()
    if "cr-db" in dblist:
        print("cr-db database and collection were created succesfully.")


def exportCollectionToJson (collection):
    # Exports collection to json file named users.json
    # args: collection - MongoDB collection object to export

    numOfDocumentsInCollection = collection.find({}).count()
    cursor = collection.find({})
    with open(EXPORT_PATH, 'w') as file:
        file.write('[')
        count = 1
        for document in cursor:
            file.write(dumps(document))
            if (count != numOfDocumentsInCollection):
                file.write(',')
            count += 1
        file.write(']')