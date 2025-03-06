from bookdata import readBooks,writeBooks

def searchBook():
    books=readBooks()
    inp=input("Enter book Title or Esbn ").lower()
    found=False
    for book in books:
        if book['title'].lower()==inp or book['isbn'].lower()==inp:
            print("Book found:",book)
            found=True
        
    if not found:
         print("No books found")   
            
