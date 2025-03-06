import json
books="books.json"

          
          



            
def readBooks():
    try:
        with open(books,"r") as read:
            return json.load(read)
    except :
            return []
        
def writeBooks(name):
    with open(books , "w") as write:
        
        return json.dump(name,write,indent=4)          
