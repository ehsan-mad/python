from bookdata import writeBooks ,readBooks

def addBooks():
    books=readBooks()
    title=input("Enter Title: ")
    author=input("Enter Author: ")
    isbn=input("Enter Isbn: ")
    for book in books:
        if book['isbn'] == isbn:
            print("Duplicate Book cannot be entered")
            return
     
    genre=input("Enter Genre: ")
    price=input("Enter price: ")
    stock=input("Enter Stock: ")
    new_book={
        "title" : title,
        "author": author,
        "isbn"  : isbn,
        "genre" : genre,
        "price" : price,
        "stock" : stock
    }    
    
    books.append(new_book)
    writeBooks(books)
    print("Book added successfully")
    
   