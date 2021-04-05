import json
import collections
from operator import itemgetter

# define constants
# EXPORT_PATH - path for exporting a data collection as a Json file from MongoDB
# DATAFILE_PATH - path to raw data file to insert to MongoDB
EXPORT_PATH = "exportData/users.json"
DATAFILE_PATH = "mongo/data.txt"


def readFile (path):
    # read file in given path and returns contents in string
    # args: path - path of file to read

    try:
        dataFile = open(path, "r")
    except Exception as e:
        return f"Could not find file to read. Exception: {e}"

    dataFileContent = dataFile.read()
    dataFile.close()
    return dataFileContent


def parseFileIntoListOfLines (fileContent):
    # returns given string in list, each entry in the list is a line in the string
    # args: fileContent - file content that should be seperated by lines

    dataFileLinesList = fileContent.split("\n")
    dataFileLinesList.pop()   # delete blank last element caused by blank line in data.txt
    return dataFileLinesList


def getDataFileListOfDicts ():
    # converts mongo/data.txt file into list of dicts and returns it

    dataFileContent = readFile(DATAFILE_PATH)
    dataFileLinesList = parseFileIntoListOfLines(dataFileContent)

    # init values to later use when inserting data into list of dicts
    dataInListOfDicts = []
    mydict = {}
    for line in dataFileLinesList:
        keyValuePairs = line.split(", ")
        for pair in keyValuePairs:
            key, value = pair.split(": ")
            mydict[key] = value
        dataInListOfDicts.append(mydict)
        mydict = {}

    return dataInListOfDicts


def capitalizeUser(document):
    # capitalize firstname and lastname in a document entry

    document['firstname'] = document['firstname'].capitalize()
    document['lastname'] = document['lastname'].capitalize()


def manipulateData():
    # iterate each document in exported collection file and performs the following:
    #    - removes object id.
    #    - capitalize string in firstName and lastname fields.
    #    - hide clear password.
    #    - sort the data by 'firstname' field.

    jsonData = json.loads(readFile(EXPORT_PATH))
    for document in jsonData:
        del document['_id']
        capitalizeUser(document)
        document['password'] = 'redacted'
    sortedJsonData = sorted(jsonData, key=itemgetter('firstname'))

    with open(EXPORT_PATH, 'w') as file:
        file.truncate()
        file.write(json.dumps(sortedJsonData))