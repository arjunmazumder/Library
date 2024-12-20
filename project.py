"""Library class"""
class Library:
    book_list=[]
    def entry_book(self, obj):
        self.book_list.append(obj)

"""Book class"""
class Book(Library):
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.__title = title
        self._author = author
        self.__availability = availability

    def borrow_book(self):
        id = input("Enter book ID to borrow : ")
        flag = True
        for book in self.book_list:
            if id == book.__book_id and book.__availability == 'available':
                book.__availability = 'Not available'
                print(f"Book '{book.__title}' borrow successfully")
                flag = False

        if flag == True:
            print("Sorry this book is unavailable")    


    def return_book(self):
        id = input("Enter book ID to return : ")
        flag = False
        for book in self.book_list:
            if id == book.__book_id and book.__availability == 'Not available':

                book.__availability = 'available'
                print(f"Book '{self.__title}' returned successfully. ")
                flag = True
        if flag == False:
            print(f'Sorry, the book ID is invalide.')

    def view_book_info(self):
        
        for info in Library.book_list:
              print(f"Id : {info.__book_id}, Title : {info.__title}, Author : {info._author}, Avilable : {info.__availability}")

book = Book('1010','C++','Herbert Schildt','available')
book.entry_book(book)
book2 = Book('1020','C','E.Balagurusamy','available')
book.entry_book(book2)
book3 = Book('1030','Java','Herbert Schildt','available')
book.entry_book(book3)
book4 = Book('1040','DSA','Seymour Lipschutz','available')
book.entry_book(book4)
book5 = Book('1050','Computer Fundamentals','Pradeep K. Sinha','available')
book.entry_book(book5)
book6 = Book('1060','Python','Eric Matthes','available')
book.entry_book(book6)
book7 = Book('1070','How to talk anyone','Eeil Lowndes','available')
book.entry_book(book7)
book8 = Book('1080','English Therapy','Saiful Islam','available')
book.entry_book(book8)
"""Menu system"""
while(True):
    print("\n************* Welcome to the Library****************\n")
    print("1. View all Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    ch = input("\n-------------------Enter your choice : ")
    print("\n")
    if ch=='1':
        book.view_book_info()
        print("\n")
    elif ch == '2':
        book.borrow_book()
        print("\n")
    elif ch == '3':
        book.return_book()  
        print("\n")  
    elif ch == '4':
        break;        


        


          
         
        
        
        