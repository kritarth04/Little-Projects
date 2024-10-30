import os 

print("Library Managment System".center(135))

class library:
    books = []
    def add_books(self):
        no = int(input("Enter how many books you want to add: "))
        while (no > 0):
            book = input("Enter the name of books : ").capitalize()
            self.books.append(book)
            no -= 1
        print(self.books)
        os.system('cls')
        self.what()

    def remove_book(self):
        print(self.books)
        num = int(input("Enter how many books you want to remove : "))
        while (num > 0):
            r_book = input("Enter the name of the book: ").capitalize()
            self.books.remove(r_book)
            num -= 1
        os.system('cls')
        self.what()

    def show_book(self):
        noOfBooks = len(self.books)
        print(noOfBooks," books are in the library")
        print(self.books)
        self.what()

    def what(self):
        what = int(input("Enter what do you intend to do \n 1- Add books \n 2- Remove books \n 3- Show books \n 4- Exit \n "))
        if (what == 1 ):
            self.add_books()
        if (what == 2 ):
            self.remove_book()
        if (what == 3 ):
            self.show_book()
        if (what == 4 ):
            os.system('cls')
            print("Thanks for using".center(170))
            
lib = library()
lib.what()

