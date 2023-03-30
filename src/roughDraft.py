import pickle, os


def initialize():
    document = open("tracker.pickle","wb")
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    lists = [row1,row2,row3,row4,row5]
    pickle.dump(lists,document)
    document.close()

def fileChecker():
    checker = os.path.isfile("tracker.pickle")
    if checker == False:
        initialize()
    
    else:
        return True


def storage(name,description,rowselection):
    fileChecker()
    
    document = open("tracker.pickle","rb")
    lists = pickle.load(document)
    lists[rowselection].append({name:description}) 
    print(lists[rowselection])
    ndocument = open("tracker.pickle","wb")
    pickle.dump(lists,ndocument)
    document.close()
    return lists[rowselection].__len__() - 1


def movement(oldrow,newrow,dicEntry):
    document = open("tracker.pickle","rb")
    lists = pickle.load(document)
    lists[newrow].append(lists[oldrow][dicEntry])
    lists[oldrow].pop(dicEntry)
    ndocument = open("tracker.pickle","wb")
    pickle.dump(lists,ndocument)
    document.close()
    return lists[newrow].__len__()-1


x = storage("Test2","Testin2g",3)
movement(3,0,x)
document = open("bugtracker.pickle","rb")
lists = pickle.load(document)
print(lists[3],lists[0])


