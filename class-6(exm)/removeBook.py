from bookdata import readBooks , writeBooks

def removeBook():
    books=readBooks()
    
    inp=input("Enter ISBN: ").trim()
    updated_books=[book for book in books if book['isbn']!=inp]
    
    
    if len(books)==len(updated_books):
        print("Book Isbn not found")
    else:
        print("The book successfully removed.")
        writeBooks(updated_books)  
        

        
         
    
