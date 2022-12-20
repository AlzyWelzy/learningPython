class Library:
    def __init__(self, books):
        self.books = books
        self.issuedbooks = []

    def displayBooks(self):
        print("Books present in the library are as follows: ")
        for book in self.books:
            print(f" *{book}")

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"The book {bookName} is available in our library and it has been lent to you. Kindly, return it in 30 days.")
            self.books.remove(bookName)
            self.issuedbooks.append(bookName)
            return True
        else:
            print("Sorry, we don't have it.")
            return False

    def returnBook(self, bookName):
        if bookName in self.issuedbooks:
            self.issuedbooks.remove(bookName)
            self.books.append(bookName)
            print(
                "Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        else:
            print(f"Sorry, We never issued {bookName} to you.")

    def issuedBooks(self):
        print("Books that are issued to you from our library are as follows: ")

        # print(len(self.issuedBooks))

        if len(self.issuedbooks) == 0:
            print("You never borrowed any books from us.")
        else:
            for book in self.issuedbooks:
                print(f" *{book}")


class Student:
    def reqBook(self):
        self.book = input("Enter the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()

    while True:
        welcomeMsg = '''
         ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Issued Books
        5. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))

        if a == 1:
            centraLibrary.displayBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.reqBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            centraLibrary.issuedBooks()
        elif a == 5:
            print("Thanks for using our services.")
            exit()
        else:
            print("ERROR")
