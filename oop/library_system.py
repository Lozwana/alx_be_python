class Book:
    def __init__(self, title: str, author: str,):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        base = super().__str__()
        return f"{base}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        base = super().__str__()
        return f"{base}, Page Count: {self.page_count}"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None