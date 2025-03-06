from bookdata import writeBooks , readBooks
def viewBook():
    books=readBooks()
    if not books:
        print("No books available")
    else:
        for book in books:
            print(f"Title:{book['title']}\nAuthor:{book['author']}\nIsbn:{book['isbn']}\nGenre:{book['genre']}\nPrice:{book['price']}\nStock:{book['stock']}\n")
    
    
