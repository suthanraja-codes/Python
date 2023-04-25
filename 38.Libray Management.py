class Library():
    def __init__(self, List):
        self.available_books = List
        self.all_books = List[:]
        self.lent_book = {}

    def available_books_list(self):
        for book in self.available_books:
            print(book)

    def all_books_list(self):
        for book in self.all_books:
            print(book)

    def borrow_book(self, name, book):
        if book not in self.all_books:
            print("Invalid Option please selece correct Book")
            return
        if book in self.available_books:
            self.lent_book.update({book:name})
            self.available_books.remove(book)
            print("You Taked The Book")
        else:
            print("This book is already Taken By , ", self.lent_book[book])

    def return_book(self,book):
        del self.lent_book[book]
        self.available_books.append(book)


if (__name__ == '__main__'):
    lib = Library(["god of war ", "clash of clans", "chin chan", "pokemon", "dragon booster"])
    print("Welcome To Library .Enter The Yorur Option")
    while True:
        print("-----------------------------------------------")
        print("1. Available Books ")
        print("2. All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Quit")
        print("-----------------------------------------------")
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            lib.available_books_list()
        elif choice == 2:
            lib.all_books_list()
        elif choice == 3:
            name = input("Enter Your Name : ")
            book = input("Enter Book Name : ")
            lib.borrow_book(name, book)
        elif choice == 4:
            book_name = input("enter The name of book : ")
            lib.return_book(book)
        elif choice == 5:
            break;
        else:
            print("Invalid Option")
