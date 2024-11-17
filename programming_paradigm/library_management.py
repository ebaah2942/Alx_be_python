class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def checked_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False
        

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else: 
            return False

    def is_available(self):
        return not self._is_checked_out        

        
        



class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, book_title):
        for book in self._books:
            if book.title == book_title:
                if book.checked_out:
                    print(f'Checked out: "{book.title}"')
                else:
                    print(f'"{book.title}" is already checked out.')
                    
               

    def return_book(self, book_title):
        for book in self._books:
            if book.title == book_title:
                if book.return_book():
                    print(f'Returned: "{book.title}"')
                    return
                else:
                    print(f'"{book.title}" is not checked out.')
                    return
                
        print(f'Book "{book.title}" not found in the library.')  



    def list_available_books(self):
       available_books = [book for book in self._books if book.is_available()]
       if available_books:
           print("Available books:")
           for book in available_books:
               print(f"- {book.title} by {book.author}")
       else:
           print("No books available.")
         


            
    

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
               return book.title



if __name__ == "__main__":
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    print(library.list_available_books())

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    print(library.list_available_books())

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    print(library.list_available_books())


