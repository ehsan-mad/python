import addBook ,removeBook,searchbook,viewBook

def menu():
    while True:
        
        print("Welcome to Book Management System")
        print("1.ADD BOOK")
        print("2.View BOOK")
        print("3.Search BOOK")
        print("4.Remove BOOK")
        print("5.Exit")
        
        choise=input("Enter Choice: ")
        if choise=="1":
            addBook.addBooks()
        elif choise=="2":
            viewBook.viewBook()
        elif choise=="3":
            searchbook.searchBook()
        elif choise=="4":
            removeBook.removeBook()
        elif choise=="5":
            print("Exiting .......")
            break       
        else:
            print("Invalid Choice")
            
menu()