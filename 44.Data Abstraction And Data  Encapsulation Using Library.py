class library:
    def __init__(self,books):
        self.books = books

    def available_books(self):
        print("Available Books...")
        for book in self.books:
            print(book)

    def borrow_books(self,borrow_books):
        print("Enter The Book To Borrow")
        if borrow_books in self.books:
            print(borrow_books)
            self.books.remove(borrow_books)
            print("You Take The Book ",borrow_books)
        else:
            print("Book Is Not Available...")

    def returned_Book(self,book):
        print("You Have Returned The Book... ",book)
        self.books.append(book)

books = ["c","c++","java"]
o = library(books)

msg = """

    1.List Of Books
    2.Borrow Books
    3.Return The Book
    
"""

while True :
    print(msg)
    ch = int(input("Enter The Choice : "))
    if ch==1:
        o.available_books()
    elif ch==2:
        book = input("ENter THe Book To Borrow : ")
        o.borrow_books(book)
    elif ch==3:
        book = input("Enter The Book To Return : ")
        o.returned_Book(book)
    else:
        print("Thank You Welcome...")
        quit()



