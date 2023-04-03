import pickle, os


def initialize():
    document = open("tracker.pickle","wb")
    lists = {}
    pickle.dump(lists,document)
    document.close()

def fileChecker():
    checker = os.path.isfile("tracker.pickle")
    if checker == False:
        initialize()
    
    else:
        return True


def storage(name,description, date, priority):
    
    hold = [name,description,date,priority]
    document = open("tracker.pickle","rb")
    lists = pickle.load(document)
    keys = len(lists) + 1
    lists[keys] = hold
    
    ndocument = open("tracker.pickle","wb")
    pickle.dump(lists,ndocument)
    document.close()

    return keys

def getData(key):
    document = open("tracker.pickle","rb")
    lists = pickle.load(document)

    #value = next(d[key] for d in lists if key in d)
    value = lists[key]
    return value

def getAllKeys():
    document = open("tracker.pickle","rb")
    lists = pickle.load(document)
    keylist = []
    keylist = list(lists.keys())
    
    return keylist

def getSpecificKey(name,description, date, priority):
    val = [name,description, date, priority]
    document = open("tracker.pickle","rb")
    lists = pickle.load(document)
    key = list(lists.values()).index(val)

def deleter(keys):
    document = open("tracker.pickle","rb")
    lists = pickle.load(document)
    lists.pop(keys)
    ndocument = open("tracker.pickle","wb")
    pickle.dump(lists,ndocument)
    document.close()
    

initialize()

storage("Test2","Testin2g","Testing", "Duh")
storage("Tes3","Tested","Testing", "Duh")
storage("Test4", "Testing","Testing", "Duh")

print(getData(1))
print(getAllKeys())
print(getSpecificKey("Test2","Testin2g","Testing", "Duh"))
document = open("tracker.pickle","rb")
lists = pickle.load(document)
print( lists)
deleter("2")
document = open("tracker.pickle","rb")
lists = pickle.load(document)
print("New List: ", lists)




