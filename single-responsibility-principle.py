'''
Написати класи, які будуть зберігати інформацію про книжки (назва книжки, імʼя автора та вартість). 
Написати код, який буде рахувати загальну вартість книжок
'''

# class Library:
#     def __init__(self) -> None:
#         self.books = []

#     def add_book(self, book_name, author_name, genre, price):
#         self.books.append([book_name, author_name, genre, price])

#     def calculate_total_price(self):
#         sum = 0
#         for book in self.books:
#             sum += book[3]
#         return sum


# library = Library()
# library.add_book("Book 1", "Author name", 100)
# print(library.calculate_total_price())

class Book:
    def __init__(self, book_name, author_name, price, genre='thriller') -> None:
        self.book_name = book_name
        self.author_name = author_name
        self.price = price
        self.discount = 0
        self.genre = genre 

    def calculate_price(self):
        return self.price - (self.price * self.discount)
    

class BookStore:
    def __init__(self) -> None:
        self.books = []
        self.shelves = []

    def sell_a_book(self, client: Client):
        pass

    def add_book(self, book: Book):
        self.books.append(book)

    def calculate_total_price(self):
        sum = 0
        for book in self.books:
            sum += book.calculate_price()
        return sum


class Client:
    def __init__(self, name) -> None:
        self.name = name

    def buy_a_book(self, book_store: BookStore):
        book_store.book[0]